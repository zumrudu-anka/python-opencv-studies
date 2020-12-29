import cv2 as cv

img = cv.imread('../resources/photos/lady.jpg')
cv.imshow('Lady', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# find face if exist and if will be found. Return top left corner with x, y; and width, height
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3)

print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness = 2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)