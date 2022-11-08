import cv2 as cv
import numpy as np

img = cv.imread('photos/city.jpg')
# cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# Laplacian

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)


# Sobel

sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)

# cv.imshow('sobel_x', sobel_x)
# cv.imshow('sobel_y', sobel_y)

combined_sobel = cv.bitwise_or(sobel_x, sobel_y)
cv.imshow('combined_sobel', combined_sobel)


canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny)


cv.waitKey(0)
