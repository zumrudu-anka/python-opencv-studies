import cv2

cap = cv2.VideoCapture("../resources/videos/kitten.mp4")

while cap.isOpened():
    ret, frame = cap.read() # ret is return value and it will be 0 or 1
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if not ret:
        break
    cv2.imshow("Gray Frame", grayFrame)
    
    key = cv2.waitKey(1)
    # u can use => key & 0xFF == ord("q") -> key & 0xFF return hexadecimal value of the key
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()