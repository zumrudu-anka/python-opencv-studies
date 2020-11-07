import cv2

cap = cv2.VideoCapture(0) # 0 to capture the webcam

while cap.isOpened():
    ret, frame = cap.read() # ret is return value and it will be 0 or 1
    if not ret:
        break
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1)
    # u can use => key & 0xFF == ord("q") -> key & 0xFF return hexadecimal value of the key
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()