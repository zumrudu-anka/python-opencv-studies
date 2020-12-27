import cv2 as cv

capture = cv.VideoCapture(0) ## From Camera

def changeRes(width, height):
    # only for live video
    capture.set(3, width)
    capture.set(4, height)

changeRes(1024, 768)

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        break
    
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()