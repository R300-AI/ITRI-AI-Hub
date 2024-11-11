import onnxruntime as ort
import numpy as np
from onnx import helper, TensorProto
import onnx, onnxsim

model_name = 'yolov8n-pose'

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
print('Pruning by following nodes:')
onnx_model = onnx.load(f'{model_name}.onnx')
intermediate_info = [edge for edge in onnx.shape_inference.infer_shapes(onnx_model).graph.value_info if edge.name.split('_output_')[0] in intermediate_nodes]
print(f'Output Result is: {[edge.name for edge in intermediate_info]}')

if 'y' in input('Is that correct?').lower():
    onnx_model = onnx.load(f'{model_name}.onnx')
    onnx_model.graph.output.clear()
    onnx_model.graph.output.extend(intermediate_info)
    onnx.checker.check_model(onnx_model)
    onnx.save(onnx_model, f'./{model_name}_phase1.onnx')
    print(f'modified ONNX saved to ./{model_name}_phase1.onnx')

#BACK
onnx_model = onnx.load(f'{model_name}.onnx')
# Add New Input Node
new_inputs = []
onnx_model.graph.input.clear()
for input_name in intermediate_nodes:
    input_info = [input_info for input_info in onnx_model.graph.value_info if input_info.name.split('_output_')[0] == input_name][0]
    input_shape = [i.dim_value for i in input_info.type.tensor_type.shape.dim]
    new_input = helper.make_tensor_value_info(input_name, TensorProto.FLOAT, input_shape)
    new_inputs.append(new_input)
onnx_model.graph.input.extend(new_inputs)

for destination in onnx_model.graph.node:
    for idx, path in enumerate(destination.input):
        for source in new_inputs:
            if source.name == path.split('_output_')[0]:
                print('Replaced inputs:')
                print(f' - source: ', source.name)
                print(f' - destination:', destination.name)
                print('--------------')
                destination.input[idx] = source.name

############################
# Remove Unued Nodes
length = 0
invalid_nodes = [i.name for i in ort.InferenceSession(f'{model_name}.onnx').get_inputs()]

while len(invalid_nodes) != length:
    length = len(invalid_nodes)
    for destination in onnx_model.graph.node:
        flag = False
        for idx, path in enumerate(destination.input):
            if path.split('_output_')[0] in invalid_nodes:
                flag = True
                
        if flag:
            print(f'Remove node {destination.name}')
            onnx_model.graph.node.remove(destination)
            if destination.name not in intermediate_nodes:
                invalid_nodes.append(destination.name)

##########################
onnx_model, check = onnxsim.simplify(onnx_model)
onnx.save(onnx_model, f'{model_name}_phase2.onnx')
print(f'modified ONNX saved to ./{model_name}_phase2.onnx')

session = ort.InferenceSession(f'{model_name}_phase2.onnx')
input_info = {i.name: i.shape for i in session.get_inputs()}
output_info = [i.name for i in session.get_outputs()]
print(input_info)
print(output_info)