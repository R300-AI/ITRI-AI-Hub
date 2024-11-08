import numpy as np
import onnxruntime as ort
import onnx

model_name = 'yolo11n-pose'
output_names = ['/model.4/Concat']

# split onnx model
onnx_model = onnx.load(f'{model_name}.onnx')
intermediate_info = [edge for edge in onnx.shape_inference.infer_shapes(onnx_model).graph.value_info]
output_protos = [edge for output in output_names for edge in intermediate_info if output in edge.name]
print(f'Output Result is: {[edge.name for edge in output_protos]}')

if 'y' in input('Is that correct?').lower():
    onnx_model.graph.output.clear()
    onnx_model.graph.output.extend(output_protos)
    onnx.checker.check_model(onnx_model)
    onnx.save(onnx_model, f'./{model_name}_modified.onnx')
    print(f'modified ONNX saved to ./{model_name}_modified.onnx')

# generate a prediction sample
ort_session = ort.InferenceSession(f'./{model_name}_modified.onnx')
input_names = {input.name: tuple(input.shape) for input in ort_session.get_inputs()}
output_names = {output.name: tuple(output.shape) for output in ort_session.get_outputs()}
print(input_names)
print(output_names)

outputs = ort_session.run(list(output_names.keys()), {input_name: np.zeros(input_names[input_name]).astype(np.float32) for input_name in input_names})
output = np.transpose(outputs[0], (0, 2, 3, 1))
print(output)
np.save('onnx_prediction', output)