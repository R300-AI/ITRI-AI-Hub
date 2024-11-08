from hailo_sdk_client import ClientRunner, InferenceContext
import numpy as np

model_name = 'yolo11n-pose'
runner = ClientRunner(hw_arch='hailo8', har=f'{model_name}.har')
with runner.infer_context(InferenceContext.SDK_HAILO_HW) as hw:
    results = runner.infer(hw, np.zeros((1, 640, 640, 3)).astype(np.uint8))

    print("Inference complete. Outputs:", results.shape)
    print(results)
    print(np.allclose(np.load('onnx_prediction.npy'), results, atol=1e-1))