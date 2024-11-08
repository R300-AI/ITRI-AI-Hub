import numpy as np
import onnxruntime as ort
import onnx

model_name = 'yolov8m-pose'
intermediate_nodes = ['/model.22/cv4.2/cv4.2.2/Conv',
                     '/model.22/cv4.1/cv4.1.2/Conv', 
                     '/model.22/cv4.0/cv4.0.2/Conv',
                     '/model.22/cv3.2/cv3.2.2/Conv',
                     '/model.22/cv3.1/cv3.1.2/Conv',
                     '/model.22/cv3.0/cv3.0.2/Conv',
                     '/model.22/cv2.2/cv2.2.2/Conv',  
                     '/model.22/cv2.1/cv2.1.2/Conv', 
                     '/model.22/cv2.0/cv2.0.2/Conv']

# FRONT
onnx_model = onnx.load(f'{model_name}.onnx')
intermediate_info = [edge for edge in onnx.shape_inference.infer_shapes(onnx_model).graph.value_info]
intermediate_protos = [edge for node in intermediate_nodes for edge in intermediate_info if node + '_output' in edge.name]
print(f'Output Result is: {[edge.name for edge in intermediate_protos]}')

if 1==1:#'y' in input('Is that correct?').lower():
    onnx_model = onnx.load(f'{model_name}.onnx')
    onnx_model.graph.output.clear()
    onnx_model.graph.output.extend(intermediate_protos)
    onnx.checker.check_model(onnx_model)
    onnx.save(onnx_model, f'./{model_name}_modified.onnx')
    print(f'modified ONNX saved to ./{model_name}_modified.onnx')

#BACK

onnx_model = onnx.load(f'{model_name}.onnx')

# Define the input and output names
node_names = ["/model.2/cv1/act/Mul", "/model.2/cv2/act/Mul"]  # Example node names

# Get the input and output tensors of the specified nodes
input_tensors = []
output_tensors = []
for node in onnx_model.graph.node:
    if node.name in node_names:
        input_tensors.extend([input_name for input_name in node.input])
        output_tensors.extend([output_name for output_name in node.output])
        
input_tensors = list(set(input_tensors)) # Remove duplicates
output_tensors = list(set(output_tensors)) # Remove duplicates

# Create an ONNX Runtime inference session
ort_session = ort.InferenceSession(f'{model_name}.onnx')

# Prepare input data (replace with actual input data)
# You'll need to create a dictionary mapping input names to NumPy arrays
# The shapes and data types of the arrays must match the model's inputs.
# Example input data:
example_input = {}
for input_name in input_tensors:
  for inp in onnx_model.graph.input:
    if inp.name == input_name:
      shape = [i.dim_value for i in inp.type.tensor_type.shape.dim]
      example_input[input_name] = np.random.rand(*shape).astype(np.float32)
      break

# Run inference
outputs = ort_session.run(output_tensors, example_input)


# Process the outputs
print("Outputs:")
for i, output_name in enumerate(output_tensors):
  print(f"  {output_name}: {outputs[i].shape}")
"""
onnx_model = onnx.load(f'{model_name}.onnx')
input_node_name = "images"
intermediate_node_names = ["/model.2/cv1/act/Mul", "/model.2/cv2/act/Mul"]

for intermediate_node_name in intermediate_node_names:
    for node in onnx_model.graph.node:
        for i, input_name in enumerate(node.input):
            if input_name == input_node_name:
                node.input[i] = intermediate_node_name
                print(f"Replaced input '{input_node_name}' with '{intermediate_node_name}' in node '{node.name}'")

new_inputs = []
for input in onnx_model.graph.input:
    if input.name != input_node_name:
        new_inputs.append(input)

for intermediate_node_name in intermediate_node_names:
    intermediate_node_found = False
    for node in onnx_model.graph.node:
        if node.name == intermediate_node_name:
            for output in node.output:
                if any(input.name == output for input in onnx_model.graph.input):
                    intermediate_node_found = True
                    break
    if not intermediate_node_found:
        for node in onnx_model.graph.node:
            if node.name == intermediate_node_name:
                new_inputs.append(onnx.helper.make_tensor_value_info(intermediate_node_name, onnx.TensorProto.FLOAT, node.output[0]))
                break

onnx_model.graph.input.clear()
onnx_model.graph.input.extend(new_inputs)
        
onnx.save(onnx_model, f'{model_name}_modified_cpu.onnx')

"""
"""
onnx_model = onnx.load(f'{model_name}.onnx')
new_inputs = []
for node in onnx_model.graph.node:
    if node.name in intermediate_nodes:
        print(node.name)
        new_inputs.append(onnx.helper.make_tensor_value_info(node.name, onnx.TensorProto.FLOAT, node.output[0]))
onnx_model.graph.input.clear()
onnx_model.graph.input.extend(intermediate_protos)
onnx.save(onnx_model, f'{model_name}_modified_cpu.onnx')
ort_session = ort.InferenceSession(f'./{model_name}_modified_cpu.onnx')

# CPU
ort_session = ort.InferenceSession(f'./{model_name}.onnx')
input_names = {output.name.split('_output_')[0]: tuple(output.shape) for output in ort.InferenceSession(f'./{model_name}_modified.onnx').get_outputs()}
output_names = {output.name: tuple(output.shape) for output in ort_session.get_outputs()}
print(input_names)
print(output_names)

outputs = ort_session.run(list(output_names.keys()), {input_name: np.zeros(input_names[input_name]).astype(np.float32) for input_name in input_names})
output = np.transpose(outputs[0], (0, 2, 3, 1))
print(output)
np.save('onnx_prediction', output)
"""