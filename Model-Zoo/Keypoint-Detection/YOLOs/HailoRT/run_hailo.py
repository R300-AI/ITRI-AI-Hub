############[Setup Hailo APIs]##############
from hailo_platform import (HEF, ConfigureParams, FormatType, HailoSchedulingAlgorithm, HailoStreamInterface,
                            InferVStreams, InputVStreamParams, InputVStreams, OutputVStreamParams, OutputVStreams,
                            VDevice)
import onnxruntime as ort
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--model_name", default='yolov8n-pose', type=str, help=".")
args = parser.parse_args()

model_name = args.model_name
session = ort.InferenceSession(f'{model_name}_end.onnx')
hef = HEF(f'{model_name}.hef')
params = VDevice.create_params()
params.scheduling_algorithm = HailoSchedulingAlgorithm.NONE
target = VDevice(params=params)
configure_params = ConfigureParams.create_from_hef(hef=hef, interface=HailoStreamInterface.PCIe)
network_groups = target.configure(hef, configure_params)
network_group = network_groups[0]
network_group_params = network_group.create_params()
input_vstreams_params = InputVStreamParams.make(network_group, quantized=False, format_type=FormatType.FLOAT32)
output_vstreams_params = OutputVStreamParams.make(network_group, quantized=True, format_type=FormatType.FLOAT32)
input_vstream_info = hef.get_input_vstream_infos()
output_vstream_info = hef.get_output_vstream_infos()
input_details, output_details =  [i for i in session.get_inputs()], [i.name for i in session.get_outputs()]
name_space = {}
for inputs_detail in output_vstream_info:
    image_height, image_width, channels = inputs_detail.shape
    for i in session.get_inputs():
        if i.shape == [1, channels, image_height, image_width]:
            name_space[inputs_detail.name] = i.name
            
def inference(input_data):
    with InferVStreams(network_group, input_vstreams_params, output_vstreams_params) as infer_pipeline:
        with network_group.activate(network_group_params):
            outputs = infer_pipeline.infer({input_vstream_info[0].name: input_data})

    inputs = {name_space[i]: np.transpose(outputs[i], (0, 3, 1, 2)).astype(np.float32) for i in outputs}
    results = session.run(output_details, inputs)
    return results[0]

############[Main]##############
from utils import preprocess, postprocess, plot
import cv2

connections = [(4, 2), (2, 0), (3, 1), (1, 0), (0, 6), (6, 8), (8, 10),
               (0, 5), (5, 7), (7, 9), (0, 12), (12, 14), (14, 16), (0, 11), (11, 13), (13, 15)]
               
frame = cv2.resize(cv2.imread('./grace_hopper.jpg'), (640, 640))
frames = np.array([frame]).astype(np.float32)

im = np.random.randint(0, 1, (1, 640, 640, 3)).astype(np.float32)
im = preprocess(frames)
preds = inference(im)
results = postprocess(preds)
print(results[0])

cv2.imshow('hef results', plot(frame.copy(), results[0].copy(), connections))
cv2.waitKey(0)
