import cv2
import pytesseract

img = cv2.imread("./assets/numplate3.jpeg")

plateHC = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),1.4)
edge = cv2.Canny(blur,50,150)
num_plates = plateHC.detectMultiScale(gray)
for x,y,w,h in num_plates:
    cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)
    detected_plate1 = gray[y : y+h, x : x+w]
    detected_plate2 = edge[y : y+h, x : x+w]
    text_plate1 = pytesseract.image_to_string(detected_plate1)
    text_plate2 = pytesseract.image_to_string(detected_plate2)
    print("Detected Text Gray:" , text_plate1)
    print("Detected Text Edges:", text_plate2)

cv2.imshow("Original Image", img)
cv2.imshow("Gray Plate", detected_plate1)
cv2.imshow("Edge Plate", detected_plate2)


cv2.waitKey(0)
cv2.destroyAllWindows()