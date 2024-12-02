# Deploy YOLOs on NeuronRT (Preview)

NeuronRT is an inference engine specifically designed for the MediaTek Genio SoC accelerator (MDLA), offering developers high-performance, low-power deep learning operations. 

To illustrate the process of delegating a model from TFLite format to an MDLA binary file (.dla), we will use the pre-built YOLOv8n model by Ultralytics as an example. This model is trained on the COCO dataset, which includes 80 classes of objects, and only supports MDLA 3.0. Follow the instructions provided in the [previous directory](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Object-Detection/YOLOs) to obtain the model on a workstation. Then, proceed with the steps outlined in this document to complete the conversion process. Finally, verify the accuracy of the inference results using a simple Python example.

### Prerequisites

* The **YOLOv8n** model in TFLite format has been exported from [[Previous Directory > Benchmarks > Train/Val Accuracy]](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Object-Detection/YOLOs).
* **Ubuntu 22.04 LTS x86_64 Workstation** with **NeuronPilot** Library installed. ([[Tutoiral]](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/compiler/neuronpilot.html))
* A **Genio-510/700 EVK (MDLA3.0)** board with **NeuronRT** Library installed. ([[Tutoiral]](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/runtime/neuronrt.html))


## Convert TFLite to DLA on Workstation

#### Step 1: Model Compilation with NeuronPilot
Use the following commands to compile a model in NeuronPilot, if you do not have NeuronPilot installed please refer to the guide [HERE](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/compiler/neuronpilot.html):

```bash
$ source deactivate && source activate neuronpilot
$ ~/neuronpilot-6.0.5/neuron_sdk/host/bin/ncc-tflite --arch=mdla3.0 --relax-fp32 ./<model_name>_saved_model/<model_name>_float32.tflite ./<model_name>_float32_mdla3.tflite
```


## Deploy Sample Codes on Board

```bash
$ git clone https://github.com/R300-AI/ITRI-AI-Hub.git && cd Model-Zoo/Detection/YOLOs/MediaTek-Genios-Demo
conda create --name YOLOs python=3.9 && source activate YOLOs
sudo pip install numpy==1.26.4 opencv-python tflite-runtime
```
