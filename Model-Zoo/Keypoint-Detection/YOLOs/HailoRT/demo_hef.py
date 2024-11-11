from hailo_platform import (HEF, ConfigureParams, FormatType, HailoSchedulingAlgorithm, HailoStreamInterface,
                            InferVStreams, InputVStreamParams, InputVStreams, OutputVStreamParams, OutputVStreams,
                            VDevice)
import numpy as np
import onnxruntime as ort

front_model_path = 'yolov8n-pose.hef'
rear_model_path = 'yolov8n-pose_rear.onnx'

session = ort.InferenceSession(rear_model_path)
input_details =  [i for i in session.get_inputs()]
output_details = [i.name for i in session.get_outputs()]


hef = HEF('yolov8n-pose.hef')

params = VDevice.create_params()
params.scheduling_algorithm = HailoSchedulingAlgorithm.NONE
target = VDevice(params=params)
configure_params = ConfigureParams.create_from_hef(hef=hef, interface=HailoStreamInterface.PCIe)
network_groups = target.configure(hef, configure_params)
network_group = network_groups[0]
network_group_params = network_group.create_params()
input_vstreams_params = InputVStreamParams.make(network_group, quantized=False, format_type=FormatType.FLOAT32)
output_vstreams_params = OutputVStreamParams.make(network_group, quantized=True, format_type=FormatType.UINT8)
input_vstream_info = hef.get_input_vstream_infos()
output_vstream_info = hef.get_output_vstream_infos()
for inputs_detail in input_vstream_info:
    image_height, image_width, channels = inputs_detail.shape
    print(inputs_detail.name, ': ', image_height, image_width, channels)


with InferVStreams(network_group, input_vstreams_params, output_vstreams_params) as infer_pipeline:
    with network_group.activate(network_group_params):
        import time
        input_data = np.random.randint(0, 1, (1, 640, 640, 3)).astype(np.float32)

        t = time.time()
        for _ in range(100):
            outputs = infer_pipeline.infer({input_vstream_info[0].name: input_data})
        print('Average inference TIme (ms):', round((time.time() -t) * 10))

for i in outputs:
    outputs[i] = np.transpose(outputs[i], (0, 3, 1, 2))
    print(i, outputs[i].shape)


#input_data = {input_vstream_info.name: dataset}