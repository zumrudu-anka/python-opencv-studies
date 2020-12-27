
###### ? Include ? ######
    
    #* Converting to GrayScale
    #* Blur
    #* Canny
    #* Dilation
    #* Erosion
    #* Resize
    #* Cropping

###### ? Include ? ######


import cv2 as cv

img = cv.imread('../resources/photos/park.jpg')
cv.imshow('Cat', img)

##### ! Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

##### ! Blur
# blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# 1. param is image
# 2. param is ksize (Mask)
# 3. param is sigmaX
cv.imshow('Blur', blur)

##### ! Edge Cascade
canny = cv.Canny(blur, 125, 175)
# 1. param is image
# 2. param is threshold1
# 3. param is threshold2
cv.imshow('Canny', canny)

# capture = cv.VideoCapture(0) ## From Camera

# while True:
#     isTrue, frame = capture.read()

#     if not isTrue:
#         break
#     newFrame = cv.Canny(frame, 125, 175)
#     cv.imshow('Video', newFrame)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

##### ! Dilating the Image
dilated = cv.dilate(canny, (3, 3), iterations = 1)
# 1. param is image
# 2. param is kernel
# 3. param is iterations
cv.imshow('Dilated', dilated)

##### ! Eroding the Image
eroded = cv.erode(dilated, (3, 3), iterations = 1)
# 1. param is image
# 2. param is kernel
# 3. param is iterations
cv.imshow('Eroded', eroded)

##### ! Resize
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)
cv.imshow('Resized', resized)

##### ! Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)