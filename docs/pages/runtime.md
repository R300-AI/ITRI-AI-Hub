---
layout: default
title: "Delegated Runtime"
nav_order: 11
---

# Deployment


## Hailo 4.18


### AMD
Vitis AI 
* Hailo data compiler==3.27
```
pip install tensorflow==1.12.0
sudo apt-get install gcc python3-dev graphviz libgraphviz-dev pkg-config

hailo -h
```
Hailo model zoo
```
conda install -c conda-forge lap
pip install numpy==1.23.3

pip -q install --upgrade fschat accelerate autoawq vllm
conda install pytorch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 cudatoolkit=10.2 -c pytorch
```



