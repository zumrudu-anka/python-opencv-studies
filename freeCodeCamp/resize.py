import cv2 as cv

def resizeFrame(frame, scale = 0.75):
    # this for images, videos and live vides
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

capture = cv.VideoCapture('../resources/videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        break
    
    resizedFrame = resizeFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Resized Video', resizedFrame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()