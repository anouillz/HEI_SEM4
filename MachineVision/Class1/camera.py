import cv2 as cv
import numpy as np

image_path = "data/left01.jpg"
image = cv.imread(image_path)
new_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

cv.imshow("image",image)
ret, corners = cv.findChessboardCorners(new_img, (9,6), None)

if ret:
    # Draw and display the corners
    cv.drawChessboardCorners(new_img, (9, 6), corners, ret)
    cv.imshow('img', new_img)

cv.waitKey(0)



