### Genio 1200
* follow instruction [HERE](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/compiler/neuronpilot.html) to install NeuronPilot
* Conda
```bash
conda create --name ultralytics python==3.12
pip install ultralytics
```
* [Train](https://docs.ultralytics.com/modes/train/) and [Export](https://docs.ultralytics.com/modes/export/#usage-examples) by Python
```bash
yolo export model=yolo11n.pt format=tflite
```
* Compile
```bash
/neuropilot-6.0.5/neuron_sdk/host/bin/ncc-tflite --arch=mdla3.0 --relax-fp32 yolov8s.tflite
```
