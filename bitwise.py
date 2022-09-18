import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')
rect = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

# cv.imshow('rect', rect)
# cv.imshow('circle', circle)

# bitwise AND --> пересекаемые области
bitwise_and = cv.bitwise_and(rect, circle)
# cv.imshow('bitwise_and', bitwise_and)

# bitwise OR --> все области
bitwise_or = cv.bitwise_or(rect, circle)
# cv.imshow('bitwise_or', bitwise_or)

# bitwise XOR --> не пересекаемые области
bitwise_xor = cv.bitwise_xor(rect, circle)
cv.imshow('bitwise_xor', bitwise_xor)

# bitwise NOT --> инвертированные области
bitwise_not = cv.bitwise_not(rect)
cv.imshow('bitwise_not', bitwise_not)

cv.waitKey(0)
