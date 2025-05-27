import cv2
cap = cv2.VideoCapture(0)
faceHC = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeHC = cv2.CascadeClassifier("haarcascade_eye.xml")

while True:
    ret,frame = cap.read() 
    if ret:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = faceHC.detectMultiScale(gray)
        for x,y,w,h in faces:
            cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            eyes = eyeHC.detectMultiScale(gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(gray, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
                cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)

    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
    cv2.imshow("Face and Eye Detection",frame)
    
cv2.waitKey(0)
cv2.destroyAllWindows()