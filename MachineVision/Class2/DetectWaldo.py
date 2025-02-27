import cv2 as cv
import numpy as np

img_path = "data/waldo_pic1.jpg"
waldo_path = "data/waldo.png"

img = cv.imread(img_path)
waldo = cv.imread(waldo_path)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sift = cv.SIFT.create()
kp1 = sift.detect(waldo, None)
kp2 = sift.detect(img, None)





output_image = cv.drawKeypoints(img, kp2, None)
cv.imwrite('sift_keypoints2.jpg', output_image)