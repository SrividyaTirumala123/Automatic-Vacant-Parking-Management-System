import cv2
import pickle
import cvzone
import torch
import numpy as np

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.conf = 0.4  # Confidence threshold

# Load the video
cap = cv2.VideoCapture(r'C:\Users\Srividya Tirumala\Downloads\CarParkProject\carPark.mp4')

# Load parking positions
with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

# Define width and height of each parking slot
width, height = 107, 48

def checkParkingSpace(imgPro, img):
    spaceCounter = 0

    for pos in posList:
        x, y = pos
        imgCrop = imgPro[y:y + height, x:x + width]
        count = cv2.countNonZero(imgCrop)

        if count < 900:
            color = (0, 255, 0)  # Green for free
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)  # Red for occupied
            thickness = 2

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1, thickness=2, offset=0, colorR=color)

    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3,
                       thickness=5, offset=20, colorR=(0, 200, 0))

while True:
    # Restart video if it ends
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()
    if not success:
        break

    # Image preprocessing
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    # Detect free/occupied slots
    checkParkingSpace(imgDilate, img)

    # Show result
    cv2.imshow("Parking Slot Detection", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



