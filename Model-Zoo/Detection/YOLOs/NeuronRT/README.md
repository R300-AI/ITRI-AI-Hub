## MediaTek Genios

### Prerequisites

* Converted `yolov8s_float_mdla3.dla` produced by [HERE](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs)
* A **Genio-510/700 EVK** board which **NeuronRT** Library has been installed.

### Demo
```bash
$ git clone https://github.com/R300-AI/ITRI-AI-Hub.git && cd Model-Zoo/Detection/YOLOs/MediaTek-Genios-Demo
conda create --name YOLOs python=3.9 && source activate YOLOs
sudo pip install numpy==1.26.4 opencv-python tflite-runtime
```
