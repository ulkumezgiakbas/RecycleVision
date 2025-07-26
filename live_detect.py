from ultralytics import YOLO
import cv2

model = YOLO('runs/detect/train3/weights/best.pt')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(source=frame, conf=0.5, save=False)

    annotated_frame = results[0].plot()

    
    cv2.imshow("RecycleVision - Live Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
