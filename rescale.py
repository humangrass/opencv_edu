import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    '''
    Метод, изменяющий размер кадра. Работает с изображениями, видео, лайв-видео.
    :param frame:
    :param scale: float value
    :return:
    '''
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    '''
    Метод, изменяющий разрешение. Работает с лайв-видео.
    :param width:
    :param height:
    :return:
    '''
    capture.set(3, width)
    capture.set(4, height)


# for photo

img = cv.imread('photos/cat.jpg')
resized_image = rescaleFrame(img, scale=0.5)
cv.imshow('Image', img)
cv.imshow('Image Resized', resized_image)

# for video

capture = cv.VideoCapture(0)  # включает вебку

# capture = cv.VideoCapture('videos/cat.mp4')     # включает видео

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 0.5)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
