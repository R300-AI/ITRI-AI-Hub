from ultralytics import YOLO
model = YOLO("yolo11n-pose.pt")
model.export(format="onnx", opset=11)

import onnx
onnx_model = onnx.load('yolo11n-pose.onnx')  # Load the exported ONNX model
print("Node Names:")
for input in onnx_model.graph.input:
  print(input.name, input.type.tensor_type.shape)
