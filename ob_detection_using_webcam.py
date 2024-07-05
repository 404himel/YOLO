from ultralytics import YOLO
import cv2
import cvzone
import math

cap = cv2.VideoCapture(0)
cap.set(3,1200)
cap.set(4,1000)
#cap = cv2.VideoCapture("Videos/1.mp4")
model = YOLO("yolov8n.pt")

#coco dataset
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

while True:
    _,img = cap.read()
    img = cv2.flip(img, 1)

    results = model(img,stream=True)
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1,y1,x2,y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1),int(y1),int(x2),int(y2)
            cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),3)

            #confident
            conf = math.ceil((box.conf[0]*100))/100
            cvzone.putTextRect(img,f'{conf}',(max(0,x1),max(25,y1)))

            #class name
            cls = int(box.cls)

            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(25, y1)))





    cv2.imshow("Img",img)
    cv2.waitKey(1)
#Himelll
