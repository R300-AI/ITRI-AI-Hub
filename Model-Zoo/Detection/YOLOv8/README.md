# Genios
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
