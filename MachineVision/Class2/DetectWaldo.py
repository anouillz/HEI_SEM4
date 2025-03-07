import cv2 as cv
import numpy as np

# Load images
img_path = "data/waldo_pic1.jpg"
waldo_path = "data/waldo.png"

img = cv.imread(img_path)
waldo = cv.imread(waldo_path)

# Convert images to grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_waldo = cv.cvtColor(waldo, cv.COLOR_BGR2GRAY)

# SIFT feature detector
sift = cv.SIFT_create()

# Detect keypoints and compute descriptors
kp1, des1 = sift.detectAndCompute(gray_waldo, None)
kp2, des2 = sift.detectAndCompute(gray_img, None)

# Feature matching using FLANN
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

flann = cv.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)

# Apply Lowe’s ratio test to filter good matches
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)

if len(good_matches) > 10:
    # Get keypoints from good matches
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    # Find homography matrix
    M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)

    if M is not None:
        # Get dimensions of Waldo image
        h, w = gray_waldo.shape
        pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
        dst = cv.perspectiveTransform(pts, M)

        # Draw rectangle around detected Waldo
        img_out = cv.polylines(img, [np.int32(dst)], isClosed=True, color=(0, 255, 0), thickness=3)

        # Save and display output
        cv.imwrite('waldo_found.jpg', img_out)
        cv.imshow("Waldo Found", img_out)
        cv.waitKey(0)

    else:
        print("No Waldo found.")
else:
    print("No Waldo found.")
