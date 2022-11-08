import os
import cv2 as cv
import numpy as np
from pathlib import Path

people = []

BASE_DIR = Path(__file__).resolve().parent
TRAIN_FACES_DIRECTORY = os.path.join(BASE_DIR, 'photos', 'Faces', 'train')

for i in os.listdir(r'{}'.format(TRAIN_FACES_DIRECTORY)):
    people.append(i)

features = []
labels = []


def create_train():
    haar_cascade = cv.CascadeClassifier('haar_face.xml')
    for person in people:
        path = os.path.join(TRAIN_FACES_DIRECTORY, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y + h, x:x + w]
                features.append(faces_roi)
                labels.append(label)


create_train()
print('TRAINING DONE --------')

features = np.array(features, dtype='object')
labels = np.array(labels)

# print(f'Length of the features = {len(features)}')
# print(f'Length of the labels = {len(labels)}')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')

np.save('features.npy', features)
np.save('labels.npy', labels)
