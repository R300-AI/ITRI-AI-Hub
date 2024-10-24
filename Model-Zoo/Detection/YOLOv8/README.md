
# Genio 1200
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


### Convert to INT32-TFLite Format
```bash
$ yolo export model=yolov8s.pt format=tflite half=True int8=True
```
* Compile by NeuronPilot
```bash
$ source deactivate && source activate neuronpilot
$ /neuronpilot-6.0.5/neuron_sdk/host/bin/ncc-tflite --arch=mdla3.0 --relax-fp32 yolov8s.tflite
```

### Convert to INT8-TFLite Format
