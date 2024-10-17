---
layout: default
title: "Model Delegation"
nav_order: 9
---

# Deployment
## Arm
* [KleidiAI - micro-kernels for Arm® CPUs](https://gitlab.arm.com/kleidi/kleidiai)
* [MLPerf Inference Suite](https://learn.arm.com/learning-paths/servers-and-cloud-computing/ml-perf/ml-perf/)

### Installation
**Step1.** Install CMake from source code.
```
sudo apt-get install libssl-dev
cd && git clone https://github.com/Kitware/CMake.git
cd Cmake
./bootstrap && make && sudo make install
```
**Step2.** Build Kleidi library for your system.
```
cd && git clone https://gitlab.arm.com/kleidi/kleidiai
cmake -DCMAKE_BUILD_TYPE=Release -S . -B build/
cmake --build ./build
```

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



