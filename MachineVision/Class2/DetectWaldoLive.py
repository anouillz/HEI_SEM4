import cv2 as cv
import numpy as np

# Load Waldo template
waldo_path = "data/waldo.png"
waldo = cv.imread(waldo_path, cv.IMREAD_GRAYSCALE)

# SIFT feature detector
sift = cv.SIFT_create()
kp1, des1 = sift.detectAndCompute(waldo, None)

# FLANN-based matcher setup
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv.FlannBasedMatcher(index_params, search_params)

# Open webcam
cap = cv.VideoCapture(0)  # 0 for default webcam

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect keypoints and compute descriptors for the frame
    kp2, des2 = sift.detectAndCompute(gray_frame, None)

    if des2 is not None and len(des2) > 0:
        # Match descriptors using FLANN
        matches = flann.knnMatch(des1, des2, k=2)

        # Apply Lowe’s ratio test
        good_matches = [m for m, n in matches if m.distance < 0.7 * n.distance]

        if len(good_matches) > 10:
            # Get keypoints from good matches
            src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

            # Find homography matrix
            M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)

            if M is not None:
                # Get dimensions of Waldo image
                h, w = waldo.shape
                pts = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
                dst = cv.perspectiveTransform(pts, M)

                # Draw rectangle around detected Waldo
                frame = cv.polylines(frame, [np.int32(dst)], isClosed=True, color=(0, 255, 0), thickness=3)

                # Print message
                print("Waldo found!")

    # Show live feed
    cv.imshow("Waldo Detector", frame)

    # Exit on 'q' key
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv.destroyAllWindows()
