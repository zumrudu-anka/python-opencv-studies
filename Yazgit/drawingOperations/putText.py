import cv2
import numpy as np

img = cv2.imread("../../resources/photos/cat.jpg")

cv2.imshow("Cat", img)

# cv2.rectangle(image, startPoint, endPoint, color, thickness)
img2 = cv2.rectangle(img, (15, 15), (625, 412), (0, 255, 0), 5)
cv2.imshow("rectangle", img2)

# cv2.circle(image, center of the circle, diameter = radius x 2, color, thickness)
img3 = cv2.circle(img2, (320, 213), 40, (0, 0, 255), 4)
cv2.imshow("Circle", img3)


# cv2.putText(image, Text, startPoint, font, fontScale, color, thickness, lineType)
# if u use gray image, u can use one channel for set the color. E.g. 129
font = cv2.FONT_HERSHEY_COMPLEX
img4 = cv2.putText(img3, "Merhaba", (50, 210), font, 4, (255, 255, 255), 4, cv2.LINE_AA)
cv2.imshow("Text", img4)

cv2.waitKey(0)
cv2.destroyAllWindows()