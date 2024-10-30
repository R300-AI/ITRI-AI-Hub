## MediaTek Genios

### Prerequisites

* Follow the Instruction [HERE](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Detection/YOLOs) to obtain `yolov8s_float_mdla3.dla`
* A **Genio-510/700 EVK** board which **NeuronRT** Library has been installed.

### Demo
```bash
conda create --name YOLOs python=3.9 && source activate YOLOs
sudo pip install numpy==1.26.4 opencv-python tflite-runtime
```
