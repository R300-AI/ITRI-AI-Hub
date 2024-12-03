from ultralytics.models.fastsam import FastSAMPredictor
import numpy as np
import time, cv2, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--model_path", default='', type=str, help="Path to ONNX file.")
args = parser.parse_args()

img = cv2.imread('./bus.jpg')

predictor = FastSAMPredictor(overrides=dict(conf=0.25, task="segment", mode="predict", model="FastSAM-s.pt", save=False, imgsz=1024))

# Prompt inference
everything_results = predictor(img)
bbox_results = predictor.prompt(everything_results, bboxes=[[200, 200, 300, 300]])
point_results = predictor.prompt(everything_results, points=[200, 200])
text_results = predictor.prompt(everything_results, texts="a photo of a dog")

cv2.imshow(results[0].plot())
