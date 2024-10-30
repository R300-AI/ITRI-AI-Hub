
# Genio 510
The yolov5 model is only supported by Genio-510/700 which use MDLA3.0 , not supported by Genio-1200, MDLA2.0.

https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/ml-guide/model-hub/YOLOv8s.html

### Prerequisites

* **Ubuntu 22.04 LTS** Workstation with **x86_64** processors and **NeuronPilot** installed. ([Installation Guide](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/compiler/neuronpilot.html))
* A **Genio-1200 EVK** board which **NeuronRT** Library has been installed.([Installation Guide](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/get-started/genio-evk.html))

## Converting Model for Deployment
### Environment and Train
* Conda
```bash
$ conda create --name ultralytics python==3.11 && source activate ultralytics
$ pip install -r requirements.txt
```
* [Train](https://docs.ultralytics.com/modes/train/) and [Export](https://docs.ultralytics.com/modes/export/#usage-examples) by Python

### Convert to INT8-TFLite Format

```bash
$ yolo export model=yolov8s.pt imgsz=640 format=torchscript
```
```bash
$ source activate neuronpilot
$ python3 convert_to_tflite_quantized.py
```

### Convert to INT32-TFLite Format
```bash
$ yolo export model=yolov8s.pt imgsz=640 format=tflite half=True int8=True
```
* Compile by NeuronPilot
```bash
$ source deactivate && source activate neuronpilot
$ ~/neuronpilot-6.0.5/neuron_sdk/host/bin/ncc-tflite --arch=mdla3.0 --relax-fp32 ./yolov8s_saved_model/yolov8s_float32.tflite
```

## Board

```bash
pip install numpy Pillow
python /usr/share/neuropilot/demo_dla/label_image.py
```

