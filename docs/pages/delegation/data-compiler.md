---
layout: default
title: "　-　Data Compiler"
nav_order: 21
---

# Hailo Model Zoo

```
conda create --name model_zoo python==3.8 && source activate model_zoo

conda install -c conda-forge lap
pip install numpy==1.23.3

pip -q install --upgrade fschat accelerate autoawq vllm
conda install pytorch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 cudatoolkit=10.2 -c pytorch
```


# Data Compiler
```
pip install tensorflow==1.12.0
sudo apt-get install gcc python3-dev graphviz libgraphviz-dev pkg-config

hailo -h
hailo tutorial
```


