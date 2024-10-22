---
layout: default
title: "　-　NCC TFLite"
nav_order: 24
---

# Install NeuronPilot for Genio Boards
##### update : 2024/10 by Markov Chen
<br>

NeuronPilot is an AI acceleration platform designed for MTK Genio SoCs for applications such as autonomous driving and industrial automation. NeuronPilot supports deep learning frameworks such as TensorFlow, PyTorch, and ONNX, and is specifically optimised for Neuron hardware to deliver the best performance and efficiency. NeuronPilot provides easy-to-use APIs and tools that enable developers to quickly deploy models to Neuron hardware for efficient inference and data processing.

## Installation
```bash
conda create --name neuronpilot python=3.7 && source activate neuronpilot
tar zxvf neuropilot-sdk-basic-6.0.5-build20240103.tar.gz
pip3 install ./neuropilot-sdk-basic-6.0.5-build20240103/offline_tool/mtk_converter-2.9.0-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.whl
pip3 install torch==1.9.0 torchvision==0.10.0

python3 -c 'import mtk_converter; print(mtk_converter.__version__)'
```
```bash
export LD_LIBRARY_PATH=/home/r300/Downloads/yolov8s/neuropilot-sdk-basic-6.0.5-build20240103/neuron_sdk/host/lib

python3 convert_to_tflite_quantized.py
```
