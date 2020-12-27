
###### ? Include ? ######
    
    #* Paint the image a certain colour
    #* Draw Rectangle
    #* Draw a Circle
    #* Draw a Line
    #* Write Text

###### ? Include ? ######

import cv2 as cv
import numpy as np

blankImage = np.zeros((500, 500, 3), dtype = 'uint8')
cv.imshow('Blank Image', blankImage)

##### ! 1. Paint the image a certain colour
blankImage[200:300, 300:400] = 0, 255, 0 # blue, green, red
#blankImage[:] = 255, 0, 0 will filled image with blue
cv.imshow('Green', blankImage)

##### ! 2. Draw Rectangle
cv.rectangle(blankImage, (0, 0), (blankImage.shape[1] // 2, blankImage.shape[0] // 2), (0, 255, 0), thickness = 2)
# cv.rectangle(blankImage, (0, 0), (250, 500), (0, 255, 0), thickness = 2)
# 1. param is Image
# 2. param is startPosition
# 3. param is height, width
# 4. param is color
# 5. param is thickness = -1 & cv.FILLED same value and max thickness. This filled the rectangle
cv.imshow('Rectangle', blankImage)

##### ! 3. Draw a Circle
cv.circle(blankImage, (blankImage.shape[1] // 2, blankImage.shape[0] // 2), 40, (0, 0, 255), thickness = -1)
# 1. param is Image
# 2. param is center of circle
# 3. param is radius of circle
# 4. param is color
# 5. param is thickness = -1 & cv.FILLED same value and max thickness. This filled the rectangle
cv.imshow('Circle', blankImage)

##### ! 4. Draw a Line
cv.line(blankImage, (10, 150), (blankImage.shape[1] // 2, blankImage.shape[0] // 2), (255, 255, 255), thickness = 3)
# 1. param is Image
# 2. param is startPosition
# 3. param is endPosition
# 4. param is color
# 5. param is thickness = -1 & cv.FILLED same value and max thickness. This filled the rectangle
cv.imshow('Line', blankImage)

##### ! 5. Write Text
blankImage2 = np.zeros((500, 500, 3), dtype = 'uint8')

cv.putText(blankImage2, 'Hello, my name is Osman!', (0, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
# 1. param is Image
# 2. param is Text
# 3. param is position
# 4. param is Font Face
# 5. param is Font Scale
# 6. param is color
# 7. param is thickness

cv.imshow('Write Text', blankImage2)

cv.waitKey(0)