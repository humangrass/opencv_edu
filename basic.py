import cv2 as cv

img = cv.imread('photos/cat.jpg')
# original image
cv.imshow('Cat', img)


# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)


# blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# gray_blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
# cv.imshow('Gray+Blur', gray_blur)


# edge cascade
canny = cv.Canny(blur, 50, 50)
# cv.imshow('Canny', canny)


# Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
# cv.imshow('Dilated', dilated)


# eroding
eroded = cv.erode(dilated, (3, 3), iterations=3)                        # обратная delate операция
# cv.imshow('Eroded', eroded)

# resize
resized = cv.resize(img, (500, 500))
cv.imshow('Resized', resized)

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_LINEAR)
# cv.imshow('Resized Linear', resized)

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)      # качество с кубик лучше
# cv.imshow('Resized Cubic', resized)


# cropping
cropped = img[200:600, 200:600]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
