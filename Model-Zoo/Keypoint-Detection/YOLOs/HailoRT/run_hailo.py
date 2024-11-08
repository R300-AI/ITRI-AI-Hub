from hailo_sdk_client import ClientRunner, InferenceContext
import numpy as np

model_name = 'yolov8m-pose'
runner = ClientRunner(hw_arch='hailo8', har=f'{model_name}.har')
with runner.infer_context(InferenceContext.SDK_HAILO_HW) as hw:
    results = runner.infer(hw, np.zeros((1, 640, 640, 3)).astype(np.uint8))
    for output in results:
        print("Inference complete. Outputs:", output.shape)
    #print(results)
    #print(np.allclose(np.load('onnx_prediction.npy'), results, atol=1e-1))