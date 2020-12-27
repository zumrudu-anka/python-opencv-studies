
###### ? Include ? ######
    
    #* Translation
    #* Rotation
    #* Resizing
    #* Flipping
    #* Cropping

###### ? Include ? ######

import cv2 as cv
import numpy as np

img = cv.imread('../resources/photos/cat.jpg')
cv.imshow('Cat', img)


#! Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    print(dimensions)
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# +x --> right
# +y --> down

# translated = translate(img, 100, 100) # --> right & down
# translated = translate(img, -100, 100) # --> left & down
# translated = translate(img, 100, -100) # --> right & up
translated = translate(img, -100, -100) # --> left & up
cv.imshow("Translated", translated)


#! Rotation
def rotate(img, angle, rotationPoint = None):
    (height, width) = img.shape[:2]
    
    if rotationPoint is None:
        rotationPoint = (width // 2, height // 2)
    
    rotMat = cv.getRotationMatrix2D(rotationPoint, angle, 1.0) # last parameter is scaling value
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

# rotated = rotate(img, 45)
rotated = rotate(img, -45)
cv.imshow("Rotated", rotated)

# rotated_rotated = rotate(rotated, -45) ## If you use it like this, you will see that some pixels are missing. 
# cv.imshow("Rotated Rotated", rotated_rotated)

rotated_rotated = rotate(img, -90)
cv.imshow("Rotated Rotated", rotated_rotated) ## Use like this.


#! Resizing
resized = cv.resize(img, (900, 900), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)


#! Flipping
# flip = cv.flip(img, 1) ## mirror image
flip = cv.flip(img, 0) ## up to bottom mirror
# flip = cv.flip(img, -1) ## mirror image and reverse up to bottom
cv.imshow("Flip", flip)


#! Cropping
cropped = img[200:400, 300:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)