import onnxruntime as ort
import numpy as np
from onnx import helper, TensorProto
import onnx, onnxsim, yaml, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--model_path", default='yolov8n-pose', type=str, help=".")
args = parser.parse_args()

model_path = args.model_path

with open('config.yaml', 'r') as f:
    config = yaml.load(f, Loader=yaml.SafeLoader)
    end_nodes = config[model_path]

    print('Pruning by following tensors:')
    onnx_model = onnx.load(f'{model_path}.onnx')
    intermediate_info = [tensor for tensor in onnx.shape_inference.infer_shapes(onnx_model).graph.value_info if tensor.name.split('_output_')[0] in end_nodes]
    for tensor in intermediate_info:
        print(' -', tensor.name)

# Pruning onnx for Hailo
if 'y' in input('Is that correct?').lower():
    onnx_model = onnx.load(f'{model_path}.onnx')
    onnx_model.graph.output.clear()
    onnx_model.graph.output.extend(intermediate_info)
    onnx.checker.check_model(onnx_model)
    onnx.save(onnx_model, f'{model_path}_front.onnx')
    print(f'Front Section of ONNX saved to {model_path}_front.onnx')

    # add new input nodes
    onnx_model = onnx.load(f'{model_path}.onnx')
    onnx_model.graph.input.clear()
    new_inputs = []
    for input_name in end_nodes:
        input_info = [input_info for input_info in onnx_model.graph.value_info if input_info.name.split('_output_')[0] == input_name][0]
        input_shape = [i.dim_value for i in input_info.type.tensor_type.shape.dim]
        new_input = helper.make_tensor_value_info(input_name, TensorProto.FLOAT, input_shape)
        new_inputs.append(new_input)
    onnx_model.graph.input.extend(new_inputs)

    # setup connection for new nodes
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
    invalid_nodes = [i.name for i in ort.InferenceSession(f'{model_path}.onnx').get_inputs()]
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
                if destination.name not in end_nodes:
                    invalid_nodes.append(destination.name)

    # save pruned model
    onnx_model, check = onnxsim.simplify(onnx_model)
    onnx.save(onnx_model, f'{model_path}_end.onnx')
    print(f'Rear Section of saved to {model_path}_end.onnx')


# Compare Origin Outpus and Concated Outputs of Pruned Model
print('Consistency Check...')
session = ort.InferenceSession(f'{model_path}.onnx')
input_details =  [i for i in session.get_inputs()]
output_details = [i.name for i in session.get_outputs()]
outputs = session

inputs = {i.name: np.zeros(i.shape).astype(np.float32) for i in input_details}
origin_results = session.run(output_details, inputs)

session_part1 = ort.InferenceSession(f'{model_path}_front.onnx')
part1_input_details =  [i for i in session_part1.get_inputs()]
part1_output_details = [i.name for i in session_part1.get_outputs()]
assert [i.name for i in input_details] == [i.name for i in part1_input_details]

for i in session_part1.get_outputs():
    print(i.name, i.shape)

inputs = {i.name: np.zeros(i.shape).astype(np.float32) for i in part1_input_details}
part1_results = session_part1.run(part1_output_details, inputs)

session_part2 = ort.InferenceSession(f'{model_path}_end.onnx')
part2_input_details =  [i for i in session_part2.get_inputs()]
part2_output_details = [i.name for i in session_part2.get_outputs()]

intermediate_inputs = {key.split('_output_')[0]: value for key, value in zip(part1_output_details, part1_results)}
part2_results = session_part2.run(part2_output_details, intermediate_inputs)
print('Passd:', np.allclose(origin_results, part2_results, rtol=1e-05, atol=1e-05))
