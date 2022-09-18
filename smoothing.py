import cv2 as cv
import numpy as np

# original image
img = cv.imread('photos/city.jpg')
# cv.imshow('Original', img)

# Averaging
average = cv.blur(img, (3, 3))
# cv.imshow('average', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3, 3), 0)
# cv.imshow('gauss', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)
