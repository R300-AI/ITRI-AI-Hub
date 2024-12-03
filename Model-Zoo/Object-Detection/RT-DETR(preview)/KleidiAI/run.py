from ultralytics import YOLO
import matplotlib.pyplot as plt
import numpy as np
import time, cv2, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--model_path", default='', type=str, help="Path to ONNX file.")
args = parser.parse_args()

img = cv2.imread('./bus.jpg')
model = YOLO(model_path=args.model_path)
results = model.predict(img, conf=0.25, iou=0.7)

print('Class:\n', [model.names[int(i.item())] for i in results[0].boxes.cls])
print('Boxes:\n', results[0].boxes.xyxy)
cv2.imshow(results[0].plot())
