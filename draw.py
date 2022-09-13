import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

# cv.imshow('Blank', blank)

# img = cv.imread('photos/cat.jpg')
# cv.imshow('Cat', img)

# draw image (square)
# blank[200:300, 300:400] = 0, 255, 0
# cv.imshow('Green', blank)

# draw rectangle
cv.rectangle(blank, (10, 10), (250, 400), (255, 0, 0), thickness=3)  # thickness - толщина границы
# cv.rectangle(blank, (10, 10), (250, 400), (0, 255, 0), thickness=-1)      # -1, чтобы заполнить весь объем
# cv.imshow('Rectangle', blank)

# draw circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 90, (0, 0, 255), thickness=-1)
# cv.imshow('Rectangle+Circle', blank)

# draw line
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=2)
# cv.imshow('Rectangle+Circle+Line', blank)


# write text
cv.putText(blank, 'Hello world', (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
cv.imshow('Rectangle+Circle+Line+Text', blank)


cv.waitKey(0)
