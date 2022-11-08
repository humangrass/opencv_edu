import cv2 as cv

img = cv.imread('photos/city.jpg')
# cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Simple Thresholding

# threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
# cv.imshow('Simple Thresholding 150', thresh)

# threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
# cv.imshow('Simple Thresholding 150 INVERSE', thresh)

# threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
# cv.imshow('Simple Thresholding 100', thresh)

# threshold, thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY)
# cv.imshow('Simple Thresholding 225', thresh)

# Adaptive thresholding

# adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
# cv.imshow('adaptive_thresh C=3', adaptive_thresh)

# adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
# cv.imshow('adaptive_thresh C=3 INVERSE', adaptive_thresh)

# adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 0)
# cv.imshow('adaptive_thresh C=0', adaptive_thresh)

# adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
# cv.imshow('adaptive_thresh boxsize=11', adaptive_thresh)

# adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 21, 3)
# cv.imshow('adaptive_thresh boxsize=21', adaptive_thresh)

cv.waitKey(0)
