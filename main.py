## Grayscale Video + Face Detection
# import cv2

# cap = cv2.VideoCapture(0)

# while True:

#     ret,frame = cap.read() 
    
#     if ret:
#         gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         faceHC = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
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

## Airplane Object Detection
# import cv2
# img1 = cv2.imread("./assets/airplaneobject1.png")
# blurred1 = cv2.GaussianBlur(img1,(5,5),1.4)
# edge1 = cv2.Canny(img1, 50, 150)
# blurred_edge1 = cv2.Canny(blurred1,50,150)
# cv2.imshow("Gaussian Blur", blurred1)
# cv2.imshow("Canny Edges", edge1)
# cv2.imshow("Gaussian Blur + Canny", blurred_edge1)

# img2 = cv2.imread("./assets/airplaneobject2.jpg")
# blurred2 = cv2.GaussianBlur(img2,(5,5),1.4)
# edge2 = cv2.Canny(img2, 50, 150)
# blurred_edge2 = cv2.Canny(blurred2,50,150)
# cv2.imshow("Gaussian Blur", blurred2)
# cv2.imshow("Canny Edges", edge2)
# cv2.imshow("Gaussian Blur + Canny", blurred_edge2)

# img3 = cv2.imread("./assets/airplaneobject3.png")
# blurred3 = cv2.GaussianBlur(img3,(5,5),1.4)
# edge3 = cv2.Canny(img3, 50, 150)
# blurred_edge3 = cv2.Canny(blurred3,50,150)
# cv2.imshow("Gaussian Blur", blurred3)
# cv2.imshow("Canny Edges", edge3)
# cv2.imshow("Gaussian Blur + Canny", blurred_edge3)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

## Live Face and Eye Detection

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
    cv2.imshow("Grayscale Face Detection",gray)
    
cv2.waitKey(0)
cv2.destroyAllWindows()
