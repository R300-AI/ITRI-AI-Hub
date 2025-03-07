import tflite_runtime.interpreter as tflite
from PIL import Image
import numpy as np
import cv2

class TFLite():
    def __init__(self, model_path):
        self.model_path = model_path
        self.interpreter = tflite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self.input_details, self.output_details = self.interpreter.get_input_details(), self.interpreter.get_output_details()
    
    def predict(self, image_path):
        inputs = np.float32([cv2.resize(cv2.imread(image_path), self.input_details[0]['shape'][1: 3], interpolation=cv2.INTER_AREA)/ 255.0])
        self.interpreter.set_tensor(self.input_details[0]['index'], inputs)
        self.interpreter.invoke()
        return self.interpreter.get_tensor(self.output_details[0]['index'])[0]

model = TFLite('./yolov8s_saved_model/yolov8s_float32.tflite')
output = model.predict('grace_hopper.jpg')
print(output.shape)
