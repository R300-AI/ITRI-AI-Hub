import onnxruntime as ort

class YOLOv8Pose():
    def __init__(self, model_path):
        self.session = ort.InferenceSession(model_path)
        self.inputs = [i for i in self.session.get_inputs()]
        self.outputs = [i.name for i in self.session.get_outputs()]

    def predict(self, frames):
        im = self.preprocess(frames)
        preds = self.inference(im)
        return preds

    def inference(self, im):
        inputs = {key.name: value for key, value in zip(self.inputs, [im])}
        preds = self.session.run(self.outputs, inputs)
        return preds

    def preprocess(self, im):
        im = np.stack(self.pre_transform(im))
        im = im[..., ::-1]
        im = np.ascontiguousarray(im).astype(np.float32)
        im /= 255.0
        return im
    
    def pre_transform(self, im):
        imgsz = self.inputs[0].shape[2:4]
        return [cv2.resize(im[0], imgsz, interpolation=cv2.INTER_LINEAR) for x in im]



import numpy as np
import cv2

frame = cv2.resize(cv2.imread('./grace_hopper.jpg'), (640, 640), interpolation=cv2.INTER_AREA)

onnx_model = YOLOv8Pose(f'yolov8n-pose.onnx')
preds = onnx_model.predict([frame])

print(preds.shape)



"""
###################################
session = ort.InferenceSession(f'{model_name}_phase1.onnx')

assert input_info == {i.name: i.shape for i in session.get_inputs()}
output_info = [i.name for i in session.get_outputs()]

outputs = session.run(output_info, dummy_input)
outputs = {key.split('_output_')[0] :value for key, value in zip(output_info, outputs)}


###################################
session = ort.InferenceSession(f'{model_name}_phase2.onnx')

input_info = {i.name.split('_output_0')[0]: i.shape for i in session.get_inputs()}
inputs = {i: outputs[i] for i in input_info}
print(input_info)
output_info = [i.name for i in session.get_outputs()]
estimated_outputs = session.run(output_info, inputs)
print(estimated_outputs.shape)
#print(output_info)"""