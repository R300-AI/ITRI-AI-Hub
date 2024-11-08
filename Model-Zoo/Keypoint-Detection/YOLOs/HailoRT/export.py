from ultralytics import YOLO
import onnx

model_name = 'yolov8n-pose'
model = YOLO(f"{model_name}.pt")
model.export(format="onnx", opset=11)

print('----------[ Profiling]----------')
onnx_model = onnx.load(f'{model_name}.onnx')

input_names = onnx_model.graph.input
node_names = onnx_model.graph.node
output_names = onnx_model.graph.output

print("Input Names:")
for input in input_names:
  print(' -', input.name, [i.dim_value for i in input.type.tensor_type.shape.dim])
print("Node Names:")
for node in node_names:
  print(' -', node.name)
print("Output Names:")
for output in output_names:
  print(' -', output.name, [i.dim_value for i in output.type.tensor_type.shape.dim])