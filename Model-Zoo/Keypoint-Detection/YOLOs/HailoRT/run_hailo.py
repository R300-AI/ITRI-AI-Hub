from hailo_sdk_client import ClientRunner, InferenceContext
import numpy as np
import onnx



    
    
onnx_model = onnx.load(f'{model_name}_phase1.onnx')
input_names = {input.name: tuple([i.dim_value for i in input.type.tensor_type.shape.dim]) for input in onnx_model.graph.input}
output_names = {output.name: tuple([i.dim_value for i in output.type.tensor_type.shape.dim]) for output in onnx_model.graph.output}


model_name = 'yolov8n-pose'
runner = ClientRunner(hw_arch='hailo8', har=f'{model_name}.har')
with runner.infer_context(InferenceContext.SDK_HAILO_HW) as hw:
    results = runner.infer(hw, np.zeros((1, 640, 640, 3)).astype(np.uint8))
    for i in output_names:
        print(i, output_names[i])

    for output in results:
        print("Inference complete. Outputs:", output.shape)
    #print(results)
    #print(np.allclose(np.load('onnx_prediction.npy'), results, atol=1e-1))