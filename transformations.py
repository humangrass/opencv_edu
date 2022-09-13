import cv2 as cv
import numpy as np


def translate(img, x, y):
    # -x --> Left
    #  x --> Right
    # -y --> Up
    #  y --> Down
    trans_mat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_mat, dimensions)


def rotate(img, angle, rot_point=None):
    (height, width) = img.shape[:2]
    if rot_point is None:
        rot_point = (width // 2, height // 2)
    rot_mat = cv.getRotationMatrix2D(rot_point, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rot_mat, dimensions)


# original image
dog = cv.imread('photos/dog.jpg')
# cv.imshow('Dog', dog)


# translation examples

# translated = translate(dog, 100, 100)
# cv.imshow('Translated: 100, 100', translated)

# translated = translate(dog, -100, -100)
# cv.imshow('Translated: -100, -100', translated)


# rotation examples

# rotated = rotate(dog, 45)
# cv.imshow('Rotated: 45', rotated)

# rotated_rotated = rotate(dog, -90)
# cv.imshow('rotated_rotated: 45', rotated_rotated)


# resizing

# resized = cv.resize(dog, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)


# flipping

flip = cv.flip(dog, 0)
cv.imshow('Flip', flip)

flip = cv.flip(dog, 1)
cv.imshow('Horizontally Flipping', flip)

flip = cv.flip(dog, -1)
cv.imshow('Reversed Horizontally Flipping', flip)


# cropping

cropped = dog[200:400, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
