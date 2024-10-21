---
layout: default
title: "　-　Data Compiler"
nav_order: 21
---

# Hailo Model Zoo
x86
```
conda create --name hailo python==3.8 && source activate hailo
sudo dpkg --install hailort-pcie-driver_4.18.0_all.deb hailort_4.18.0_amd64.deb
pip install hailort-4.18.0-cp38-cp38-linux_x86_64.whl
```
```
hailo -h
hailo tutorial
```

# None
conda install -c conda-forge lap
pip install numpy==1.23.3

pip -q install --upgrade fschat accelerate autoawq
conda install pytorch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 cudatoolkit=10.2 -c pytorch
# Data Compiler
```
pip install tensorflow==1.12.0
sudo apt-get install gcc python3-dev graphviz libgraphviz-dev pkg-config

hailo -h
hailo tutorial
```

# 4.17
```
conda create --name hailo python=3.8 && source activate hailo
```
### x86
```
sudo dpkg --install hailort-pcie-driver_4.17.0_all.deb
sudo dpkg --install hailort_4.17.0_amd64.deb -y
pip install hailort-4.17.0-cp38-cp38-linux_x86_64.whl
```
```
pip install hailo_dataflow_compiler-3.27.0-py3-none-linux_x86_64.whl
```
```
hailo h
hailo tutorial
```


