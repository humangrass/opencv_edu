import cv2 as cv

# read img

# img = cv.imread('photos/cat.jpg')
#
# cv.imshow('Cat', img)
#
# cv.waitKey(0)

# read video

capture = cv.VideoCapture(0)                  # включает вебку

# capture = cv.VideoCapture('videos/cat.mp4')     # включает видео

while True:
    isTrue, frame = capture.read()
    canny = cv.Canny(frame, 100, 100)
    cv.imshow('Video', canny)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
