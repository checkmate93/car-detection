from ultralytics import YOLO
import cv2
import cvzone
import math
import time

#cap = cv2.VideoCapture(1) # for webcam
cap = cv2.VideoCapture(r"video\cars.mp4")

cap.set(3, 1280)
cap.set(4, 720)

model = YOLO("yolov8n.pt")
classNames = model.names  # χρησιμοποιεί τις default 80 κλάσεις COCO

while True:
    success, image = cap.read()
    if not success:
        break

    results = model(image, stream=True)  # χρήση stream για αποδοτικό loop

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            w, h = x2 - x1, y2 - y1

            cvzone.cornerRect(image, (x1, y1, w, h), l=9, rt=3)

            conf = round(float(box.conf[0]), 2)
            cls = int(box.cls[0])
            currentClass=classNames[cls]

            if currentClass == "car" or currentClass=="truck" or currentClass==("motorbike") and conf > 0.5:


                label = classNames.get(cls, "Unknown")

            cvzone.putTextRect(image, f'{label} {conf}',
                               (max(0, x1), max(35, y1)), scale=1, thickness=1,offset=3)

    cv2.imshow("Detected", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()