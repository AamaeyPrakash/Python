

import cv2
import face_recognition
import os
faceHC = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
cap = cv2.VideoCapture(0)

knownFaceEncoding = []
knownFaceNames = []

for fileName in os.listdir("KnownFaces"):
    image = face_recognition.load_image_file("KnownFaces/"+fileName)
    encoding = face_recognition.face_encodings(image)[0]
    knownFaceEncoding.append(encoding)
    knownFaceNames.append(os.path.splitext(fileName)[0])

while True:
    ret,frame = cap.read()
    if not ret:
        break
