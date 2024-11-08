import numpy as np
import onnxruntime as ort
from onnx import helper, TensorProto
import onnx

model_name = 'yolov8n-pose'
intermediate_nodes = ['/model.2/cv1/conv/Conv']
"""
intermediate_nodes = ['/model.22/cv4.2/cv4.2.2/Conv',
                     '/model.22/cv4.1/cv4.1.2/Conv', 
                     '/model.22/cv4.0/cv4.0.2/Conv',
                     '/model.22/cv3.2/cv3.2.2/Conv',
                     '/model.22/cv3.1/cv3.1.2/Conv',
                     '/model.22/cv3.0/cv3.0.2/Conv',
                     '/model.22/cv2.2/cv2.2.2/Conv',  
                     '/model.22/cv2.1/cv2.1.2/Conv', 
                     '/model.22/cv2.0/cv2.0.2/Conv']
"""
# FRONT
onnx_model = onnx.load(f'{model_name}.onnx')
intermediate_info = [edge for edge in onnx.shape_inference.infer_shapes(onnx_model).graph.value_info if edge.name.split('_output_')[0] in intermediate_nodes]
print(f'Output Result is: {[edge.name for edge in intermediate_info]}')

if 1==1: #'y' in input('Is that correct?').lower():
    onnx_model = onnx.load(f'{model_name}.onnx')
    onnx_model.graph.output.clear()
    onnx_model.graph.output.extend(intermediate_info)
    onnx.checker.check_model(onnx_model)
    onnx.save(onnx_model, f'./{model_name}_modified.onnx')
    print(f'modified ONNX saved to ./{model_name}_modified.onnx')

#BACK
onnx_model = onnx.load(f'{model_name}.onnx')
connections = {edge.name: tuple(edge.shape) for edge in ort.InferenceSession(f'./{model_name}_modified.onnx').get_outputs()}
#print(connections)

new_inputs = []
onnx_model.graph.input.clear()
for input_name in intermediate_nodes:
    input_info = [input_info for input_info in onnx_model.graph.value_info if input_info.name.split('_output_')[0] == input_name][0]
    input_shape = [i.dim_value for i in input_info.type.tensor_type.shape.dim]
    print(input_name, input_shape)

    new_input = helper.make_tensor_value_info(input_name, TensorProto.FLOAT, input_shape)
    new_inputs.append(new_input)
onnx_model.graph.input.extend(new_inputs)

print('=============')
# Replace the input data of the old intermediate node with the new input tensor
for node in onnx_model.graph.node:
    for idx, input_name in enumerate(node.input):
        if input_name == input_info.name:
            node.input[idx] = new_input.name
            print(f'Replaced input {input_info.name} with {new_input.name} in node {node.name}')

onnx.save(onnx_model, f'{model_name}_modified_cpu.onnx')
print(f'modified ONNX saved to ./{model_name}_modified_cpu.onnx')

# CPU
"""
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