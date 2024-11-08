from hailo_platform import (HEF, ConfigureParams, FormatType, HailoSchedulingAlgorithm, HailoStreamInterface,
                            InferVStreams, InputVStreamParams, InputVStreams, OutputVStreamParams, OutputVStreams,
                            VDevice)
import numpy as np

params = VDevice.create_params()
params.scheduling_algorithm = HailoSchedulingAlgorithm.NONE
target = VDevice(params=params)

model_name = 'yolo11n-pose'
hef = HEF(f'{model_name}.hef')

configure_params = ConfigureParams.create_from_hef(hef=hef, interface=HailoStreamInterface.PCIe)
network_groups = target.configure(hef, configure_params)
network_group = network_groups[0]
network_group_params = network_group.create_params()

input_vstreams_params = InputVStreamParams.make(network_group, quantized=False, format_type=FormatType.FLOAT32)
output_vstreams_params = OutputVStreamParams.make(network_group, quantized=True, format_type=FormatType.UINT8)

input_vstream_info = hef.get_input_vstream_infos()[0]
output_vstream_info = hef.get_output_vstream_infos()[0]
image_height, image_width, channels = input_vstream_info.shape

dataset = np.random.randint(0, 1, (1, image_height, image_width, channels)).astype(np.float32)
input_data = {input_vstream_info.name: dataset}

with InferVStreams(network_group, input_vstreams_params, output_vstreams_params) as infer_pipeline:
    with network_group.activate(network_group_params):
        import time
        t = time.time()
        for _ in range(100):
            infer_results = infer_pipeline.infer(input_data)
            print('shape:', infer_results[output_vstream_info.name].shape)
        print('Inference TIme (ms):', round((time.time() -t) * 10))