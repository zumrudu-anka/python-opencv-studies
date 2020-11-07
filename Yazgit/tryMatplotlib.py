import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("../resources/photos/cat.jpg", 0)

plt.imshow(img, cmap = "gray", interpolation="bicubic")

# If u won't use this two line, u can see x, y ticks on window
plt.xticks([])
plt.yticks([])
#

plt.show()
