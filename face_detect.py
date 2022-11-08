import cv2 as cv

# img = cv.imread('photos/group_2.jpg')
# # cv.imshow('Original', img)
#
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# # cv.imshow('gray', gray)
#
# haar_cascade = cv.CascadeClassifier('haar_face.xml')
# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
#
# print(f'Number of faces found = {len(faces_rect)}')
#
# for (x, y, w, h) in faces_rect:
#     cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
#
# cv.imshow('Detected Faces', img)
#
# cv.waitKey(0)


capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    haar_cascade = cv.CascadeClassifier('haar_face.xml')
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
    cv.imshow('Detected Faces on Video', frame)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
