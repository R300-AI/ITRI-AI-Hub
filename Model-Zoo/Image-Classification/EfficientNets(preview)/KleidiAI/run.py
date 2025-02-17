import onnxruntime as ort
import numpy as np
import cv2

def preprocess(image_path):
  img = cv2.imread(image_path)
  img = cv2.resize(img, (224, 224))
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) / 255.0
  img = np.expand_dims(img.astype(np.float32), axis=0)
  return np.transpose(img, (0, 3, 1, 2))

with open('imagenet-classes.txt', 'r') as f:
    CLASSES = [line.strip() for line in f.readlines()]
CLASSES

inputs = preprocess("grace_hopper.jpg")
ort_session = ort.InferenceSession("resnet18.onnx")
results = ort_session.run(None, {ort_session.get_inputs()[0].name: inputs})

print(CLASSES[np.argmax(results[0])])
