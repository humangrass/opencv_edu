import cv2 as cv
import numpy as np

img = cv.imread('photos/dog.jpg')
# cv.imshow('Original', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv.circle(blank.copy(), (img.shape[1] // 2 + 80, img.shape[0] // 2), 200, 255, -1)
# cv.imshow('mask', mask)

masked = cv.bitwise_and(img, img, mask=circle)
cv.imshow('masked', masked)

rect = cv.rectangle(blank.copy(), (30, 30), (570, 570), 255, -1)

weird_shape = cv.bitwise_and(circle, rect)
# cv.imshow('weird_shape', weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('weird_shape masked', masked)

cv.waitKey(0)
