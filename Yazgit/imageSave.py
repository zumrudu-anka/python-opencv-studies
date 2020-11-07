import cv2
import numpy as np

#img = cv2.imread("../resources/photos/cat.jpg", -1) # with alpha channel
img = cv2.imread("../resources/photos/cat.jpg", 0) # gray
#img = cv2.imread("../resources/photos/cat.jpg", 1) # original

cv2.imshow("Cat", img)

key = cv2.waitKey(0)
if key == 27: # 27 is hexadecimal value of the esc
    cv2.destroyAllWindows()
elif key == ord("s"):
    cv2.imwrite("./outputs/gray_cat2.jpg", img) # e.g. deneme.png, deneme.bmp