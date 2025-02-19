import onnxruntime as ort
import cv2
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--model_path", default='', type=str, help="Path to ONNX file.")
args = parser.parse_args()

img = cv2.imread("bus.jpg")
ort_session = ort.InferenceSession(args.model_path)

inputs = cv2.resize(img, ort_session.get_inputs()[0].shape[1: 3])
outputs = ort_session.run(None, {ort_session.get_inputs()[0].name: np.expand_dims(inputs, axis=0).astype(np.uint8)})

scores = np.squeeze(outputs[0])
boxes = np.squeeze(outputs[1])
count = int(np.squeeze(outputs[2]))
classes = np.squeeze(outputs[3])

for i in range(count):
  score, box, cls = scores[i], boxes[i], classes[i]
  print('Class:', cls, 'with conf', score)
  print('Boxes:\n', box)
  
