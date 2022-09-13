import cv2 as cv
import matplotlib.pyplot as plt

# original image
img = cv.imread('photos/dog.jpg')
# cv.imshow('Original', img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('hsv', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('lab', lab)

# BGT to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

# plt.imshow(rgb)
# plt.show()

# HSV to BGR
bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('bgr', bgr)

cv.waitKey(0)
