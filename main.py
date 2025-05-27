## Grayscale Video + Face Detection
# import cv2
# cap = cv2.VideoCapture(0)

# while True:

#     ret,frame = cap.read() 
    
#     if ret:
#         gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         faceHC = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         faces = faceHC.detectMultiScale(gray)
#         for x,y,w,h in faces:
#             cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),2)

#     if cv2.waitKey(2) & 0xFF == ord('q'):
#         break
#     cv2.imshow("Grayscale Face Detection",gray)
    
# cv2.waitKey(0)
# cv2.destroyAllWindows()

## Video Capture Gaussian + Canny
# import cv2
# cap = cv2.VideoCapture(0)

# while True:

#     ret,frame = cap.read() 
    
#     if ret:
#         blurred = cv2.GaussianBlur(frame,(5,5),1.4)
#         edge = cv2.Canny(blurred,50,150)
#         edge2 = cv2.Canny(frame,50,150)
#     if cv2.waitKey(2) & 0xFF == ord('q'):
#         break
#     cv2.imshow("Gaussian Blur",blurred)
#     cv2.imshow("Canny + Gaussian Blur", edge)
#     cv2.imshow("Canny Edges", edge2)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

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