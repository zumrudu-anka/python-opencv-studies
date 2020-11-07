import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

cv2.imshow("Black Background", img)


# cv2.line(image, startPoint, endPoint, color with rgb, thickness)
img2 = cv2.line(img, (0, 0), (512, 512), (255, 0, 0), 6)

cv2.imshow("Blue Diagonal", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()