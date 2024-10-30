import subprocess, re, logging
from utils import DLAInfo
import cv2
import numpy as np

class DLA():
    def __init__(self, model_path):
        self.model_path = model_path
        self.inputs = 'input.bin'
        self.intput_size, self.outputs = DLAInfo(model_path)
        self.cmd = f"neuronrt -m hw -a {self.model_path} -c 1 -b 100 -i {self.inputs} -o {' '.join(self.outputs)}"
        print(self.cmd)
        
    def predict(self, image_path):
        self.img_to_bin(image_path)
        res = subprocess.run(self.cmd, shell=True, check=True, executable='/bin/bash', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        outputs = [np.fromfile(output) for output in self.outputs]
        print(outputs[0].shape)
        
    def img_to_bin(self, image_path):
        img = cv2.resize(cv2.imread(image_path), self.intput_size[1:3], interpolation=cv2.INTER_AREA)
        img = np.float32([img / 255.0])
        print()
        assert img.shape == self.intput_size
        img.tofile(self.inputs);
        return self.inputs

model = DLA(model_path = './yolov8s_saved_model/yolov8s_float32.dla')
model.predict('grace_hopper.jpg')
