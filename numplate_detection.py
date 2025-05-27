import cv2
import pytesseract

img = cv2.imread("./assets/numplate1.png") 
text = pytesseract.image_to_string(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),1.4)
edge = cv2.Canny(blur,50,150)

text2 = pytesseract.image_to_string(edge)

cv2.imshow("Original Image", img)
cv2.imshow("Blur + Edge", edge)

print("Detected Text:", text)
print("Detected Text 2:", text2)

cv2.waitKey(0)
cv2.destroyAllWindows()