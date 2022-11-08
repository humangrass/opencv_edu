import os
import cv2 as cv
import numpy as np
from pathlib import Path


haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

# people
people_train = []
people_val = []

BASE_DIR = Path(__file__).resolve().parent
TRAIN_FACES_DIRECTORY = os.path.join(BASE_DIR, 'photos', 'Faces', 'train')
VALIDATION_FACES_DIRECTORY = os.path.join(BASE_DIR, 'photos', 'Faces', 'val')

for i in os.listdir(r'{}'.format(TRAIN_FACES_DIRECTORY)):
    people_train.append(i)

for i in os.listdir(r'{}'.format(VALIDATION_FACES_DIRECTORY)):
    people_val.append(i)

filenames = []
for i in os.listdir(r'{}\{}'.format(VALIDATION_FACES_DIRECTORY, people_val[0])):
    filenames.append(i)


img = cv.imread(r'{path}\{person}\{img}'.format(path=VALIDATION_FACES_DIRECTORY, person=people_val[3], img=filenames[2]))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Person', gray)

# detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people_train[label]} with a confidence of {confidence}')

    cv.putText(img, str(people_train[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
cv.imshow('Detecting Face', img)

cv.waitKey(0)
