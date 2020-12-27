import cv2 as cv

## ! Reading Images

# img = cv.imread('../resources/photos/cat_large.jpg')

# cv.imshow('Cat', img)

# cv.waitKey(0)

## ! Reading Videos

# capture = cv.VideoCapture(0) ## From Camera
capture = cv.VideoCapture('../resources/videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        break

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()