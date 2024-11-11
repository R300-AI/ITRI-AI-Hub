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


# Pruning onnx for Hailo
print('Pruning by following tensors:')

onnx_model = onnx.load(f'{model_name}.onnx')
intermediate_info = [tensor for tensor in onnx.shape_inference.infer_shapes(onnx_model).graph.value_info if tensor.name.split('_output_')[0] in intermediate_nodes]
for tensor in intermediate_info:
    print(' -', tensor.name)

if 'y' in input('Is that correct?').lower():
    onnx_model = onnx.load(f'{model_name}.onnx')
    onnx_model.graph.output.clear()
    onnx_model.graph.output.extend(intermediate_info)
    onnx.checker.check_model(onnx_model)
    onnx.save(onnx_model, f'./{model_name}_front.onnx')
    print(f'Front Section of ONNX saved to ./{model_name}_front.onnx')

    # add new input nodes into ONNX
    onnx_model = onnx.load(f'{model_name}.onnx')
    onnx_model.graph.input.clear()
    new_inputs = []
    for input_name in intermediate_nodes:
        input_info = [input_info for input_info in onnx_model.graph.value_info if input_info.name.split('_output_')[0] == input_name][0]
        input_shape = [i.dim_value for i in input_info.type.tensor_type.shape.dim]
        new_input = helper.make_tensor_value_info(input_name, TensorProto.FLOAT, input_shape)
        new_inputs.append(new_input)
    onnx_model.graph.input.extend(new_inputs)
    # setup connection
    for destination in onnx_model.graph.node:
        for idx, path in enumerate(destination.input):
            for source in new_inputs:
                if source.name == path.split('_output_')[0]:
                    print('Replaced inputs:')
                    print(f' - source: ', source.name)
                    print(f' - destination:', destination.name)
                    print('--------------')
                    destination.input[idx] = source.name

    # remove unused nodes
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
    onnx_model, check = onnxsim.simplify(onnx_model)
    onnx.save(onnx_model, f'{model_name}_rear.onnx')
    print(f'Rear Section of saved to ./{model_name}_rear.onnx')

print('Consistency Check...')
# Origin
session = ort.InferenceSession(f'{model_name}.onnx')
input_details =  [i for i in session.get_inputs()]
output_details = [i.name for i in session.get_outputs()]
outputs = session

inputs = {i.name: np.zeros(i.shape).astype(np.float32) for i in input_details}
results = session.run(output_details, inputs)

# Pruned
session_part1 = ort.InferenceSession(f'{model_name}_front.onnx')
part1_input_details =  [i for i in session_part1.get_inputs()]
part1_output_details = [i.name for i in session_part1.get_outputs()]
assert [i.name for i in input_details] == [i.name for i in part1_input_details]

for i in session_part1.get_outputs():
    print(i.name, i.shape)

inputs = {i.name: np.zeros(i.shape).astype(np.float32) for i in part1_input_details}
part1_results = session_part1.run(part1_output_details, inputs)

session_part2 = ort.InferenceSession(f'{model_name}_rear.onnx')
part2_input_details =  [i for i in session_part2.get_inputs()]
part2_output_details = [i.name for i in session_part2.get_outputs()]

intermediate_inputs = {key.split('_output_')[0]: value for key, value in zip(part1_output_details, part1_results)}
part2_results = session_part2.run(part2_output_details, intermediate_inputs)
print('Passd:', np.allclose(results, part2_results, rtol=1e-05, atol=1e-05))