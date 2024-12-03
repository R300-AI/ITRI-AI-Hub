from ultralytics import FastSAM
import numpy as np
import time, cv2, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--model_path", default='', type=str, help="Path to ONNX file.")
args = parser.parse_args()

img = cv2.imread('./bus.jpg')

# Run inference with bboxes prompt
results = model(img, bboxes=[439, 437, 524, 709])
print('Class:\n', [model.names[int(i.item())] for i in results[0].boxes.cls])
print('Masks:\n', results[0].masks.xy)
cv2.imshow(results[0].plot())

# Run inference with points prompt
results = model(img, points=[[200, 200]], labels=[1])
print('Class:\n', [model.names[int(i.item())] for i in results[0].boxes.cls])
print('Masks:\n', results[0].masks.xy)
cv2.imshow(results[0].plot())

# Run inference with texts prompt
results = model(img, texts="a photo of a dog")
print('Class:\n', [model.names[int(i.item())] for i in results[0].boxes.cls])
print('Masks:\n', results[0].masks.xy)
cv2.imshow(results[0].plot())
