import cv2
import numpy as np

#img = cv2.imread("../resources/photos/cat.jpg", -1) # with alpha channel
img = cv2.imread("../resources/photos/cat.jpg", 0) # gray
#img = cv2.imread("../resources/photos/cat.jpg", 1) # original


cv2.imshow("Cat", img)
cv2.waitKey(0)
cv2.destroyAllWindows()