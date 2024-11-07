from hailo_sdk_client import ClientRunner
import numpy as np

input_names = {'/model.0/conv/Conv': [1, 3, 640, 640]}
output_names = ['/model.4/cv2/conv/Conv']

model_name = 'yolo11n-pose'
onnx_path = './yolo11n-pose.onnx'

runner = ClientRunner(hw_arch='hailo8')
hn, npz = runner.translate_onnx_model(onnx_path, model_name,
                                      start_node_names=list(input_names.keys()),
                                      end_node_names=output_names,
                                      net_input_shapes=input_names)


batch_size = 10
calib_dataset = np.zeros((batch_size, 640, 640, 3))
np.save('calib_set.npy', calib_dataset)

runner.optimize(calib_dataset)
hef = runner.compile()

file_name = f'{model_name}.hef'
with open(file_name, 'wb') as f:
    f.write(hef)

hailo_model_har_name = f'{model_name}.har'
runner.save_har(hailo_model_har_name)
    
