import cv2 as cv
import numpy as np

# original image
img = cv.imread('photos/city.jpg')
# cv.imshow('Original', img)

blue, green, red = cv.split(img)
blank = np.zeros(img.shape[:2], dtype='uint8')

# cv.imshow('blue', blue)
# cv.imshow('green', green)
# cv.imshow('red', red)

print(img.shape)
print(blue.shape)
print(green.shape)
print(red.shape)

# merged = cv.merge([red, green, red])
# cv.imshow('RGR', merged)
#
# merged = cv.merge([red, blue, green])
# cv.imshow('RBG', merged)

blue = cv.merge([blank, blank, blue])
green = cv.merge([blank, green, blank])
red = cv.merge([red, blank, blank])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

cv.waitKey(0)
