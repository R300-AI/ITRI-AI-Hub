from hailo_sdk_client import ClientRunner
from utils import preprocess
import numpy as np
import onnx, subprocess, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--model_path", default='yolov8n-pose', type=str, help=".")
args = parser.parse_args()

model_path = args.model_path

calibration_size = 1024
onnx_model = onnx.load(f'{model_path}_front.onnx')
input_names = {input.name: tuple([i.dim_value for i in input.type.tensor_type.shape.dim]) for input in onnx_model.graph.input}
output_names = {output.name: tuple([i.dim_value for i in output.type.tensor_type.shape.dim]) for output in onnx_model.graph.output}

runner = ClientRunner(hw_arch='hailo8')
hn, npz = runner.translate_onnx_model(f'{model_path}_front.onnx', model_path,
                                    start_node_names=list(input_names.keys()),
                                    end_node_names=list(output_names.keys()),
                                    net_input_shapes=list(input_names.values()))

samples = np.random.randint(0, 255, (calibration_size, 640, 640, 3)).astype(np.float32)
calib_dataset = preprocess(samples)

model_script_commands = [
    f'model_optimization_config(calibration, calibset_size={calibration_size})\n',
    'model_optimization_flavor(optimization_level=0)\n',
]
runner.load_model_script(''.join(model_script_commands))
runner.optimize(calib_dataset)

hef = runner.compile()

with open(f'{model_path}.hef', 'wb') as f:
    f.write(hef)
runner.save_har(f'{model_path}.har')

subprocess.run(["hailo", "profiler", f'{model_path}.har']) 
