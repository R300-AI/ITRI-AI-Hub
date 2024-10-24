### Genio 1200
* follow instruction [HERE](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/compiler/neuronpilot.html) to install NeuronPilot

* Train and Export
```
from ultralytics import YOLO

model = YOLO("yolo11n.pt")
model.export(format="tflite")
```
```
yolo export model=yolo11n.pt format=onnx  # export official model
```
* Compile
```
/neuropilot-6.0.5/neuron_sdk/host/bin/ncc-tflite --arch=mdla3.0 --relax-fp32 yolov8s.tflite
```
