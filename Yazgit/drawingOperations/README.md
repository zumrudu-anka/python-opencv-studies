### Draw a Line on the Image:
- cv2.line(image, startPoint, endPoint, color with rgb, thickness)
> e.g. `img = cv2.line(img, (0, 0), (512, 512), (255, 0, 0), 6)`

### Draw a Rectangle on the Image:
- cv2.rectangle(image, startPoint, endPoint, color, thickness)
> e.g. `img = cv2.rectangle(img, (15, 15), (625, 412), (0, 255, 0), 5)`

### Draw a Circle on the Image:
- cv2.circle(image, center of the circle, diameter = radius x 2, color, thickness)
> e.g. `img = cv2.circle(img2, (320, 213), 40, (0, 0, 255), 4)`

### Put text on the Image:
- cv2.putText(image, Text, startPoint, font, fontScale, color, thickness, lineType)
> e.g. `img = cv2.putText(img3, "Merhaba", (50, 210), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 255, 255), 4, cv2.LINE_AA)`