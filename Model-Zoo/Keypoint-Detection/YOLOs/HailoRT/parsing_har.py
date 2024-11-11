from hailo_sdk_client import ClientRunner
import numpy as np
import onnx, subprocess

model_name = 'yolov8n-pose'
calibration_size = 100
onnx_model = onnx.load(f'{model_name}_phase1.onnx')
input_names = {input.name: tuple([i.dim_value for i in input.type.tensor_type.shape.dim]) for input in onnx_model.graph.input}
output_names = {output.name: tuple([i.dim_value for i in output.type.tensor_type.shape.dim]) for output in onnx_model.graph.output}
print(input_names)
print(output_names)

runner = ClientRunner(hw_arch='hailo8')
hn, npz = runner.translate_onnx_model(f'./{model_name}_phase1.onnx', model_name,
                                    start_node_names=list(input_names.keys()),
                                    end_node_names=list(output_names.keys()),
                                    net_input_shapes=list(input_names.values()))


calib_dataset = np.random.randint(0, 1, (calibration_size, 640, 640, 3)).astype(np.uint8)
runner.optimize(calib_dataset)
hef = runner.compile()

with open(f'{model_name}.hef', 'wb') as f:
    f.write(hef)
runner.save_har(f'{model_name}.har')
subprocess.run(["hailo", "profiler", f'{model_name}.har']) 