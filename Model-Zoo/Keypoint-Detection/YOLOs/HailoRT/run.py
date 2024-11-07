from hailo_sdk_client import ClientRunner
from hailo_sdk_client import InferenceContext
import numpy as np

compiled_model_har_path = 'yolo11n-pose.har'
runner = ClientRunner(hw_arch='hailo8', har=compiled_model_har_path)

with runner.infer_context(InferenceContext.SDK_HAILO_HW) as hw:
    for i in range(100):
        dataset = np.random.randint(0, 1, (1, 640, 640, 3)).astype(np.uint8)
        results = runner.infer(hw, dataset)
