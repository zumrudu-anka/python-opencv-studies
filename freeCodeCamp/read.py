import cv2 as cv

img = cv.imread('../resources/photos/cat.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)