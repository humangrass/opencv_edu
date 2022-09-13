import cv2 as cv
import numpy as np

# original image
img = cv.imread('photos/dogs.jpg')
# cv.imshow('Original', img)


# resize
resized = cv.resize(img, (1000, 600), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

blank = np.zeros(resized.shape, dtype='uint8')
# cv.imshow('blank', blank)

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray, (7, 7), cv.BORDER_DEFAULT)

ret, thresh = cv.threshold(blur, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)

# wrong way
# blank2 = np.zeros(resized.shape, dtype='uint8')
# canny = cv.Canny(blur, 100, 130)
# cv.imshow('canny', canny)
#
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(f'{len(contours)} contours found')
#
# cv.drawContours(blank2, contours, -1, (0, 0, 255), 1)
# cv.imshow('Contours_canny', blank2)

cv.waitKey(0)

