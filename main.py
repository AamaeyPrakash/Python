import cv2

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read() 
    if ret:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faceHC = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
        faces = faceHC.detectMultiScale(gray)
        for x,y,w,h in faces:
            cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),2)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
    cv2.imshow("Face Detection",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()