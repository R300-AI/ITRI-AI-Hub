---
layout: default
title: "Model Delegation"
nav_order: 9
---

# Deployment
Vitis AI 
Hailo data compiler==3.27
```
pip install tensorflow==1.12.0
sudo apt-get install gcc python3-dev graphviz libgraphviz-dev pkg-config

hailo -h
```
Hailo model zoo
```
conda install -c conda-forge lap
```


Kleidi AI
```
sudo apt-get install libssl-dev
git clone https://github.com/Kitware/CMake.git
cd Cmake
./bootstrap && make && sudo make install

git clone https://gitlab.arm.com/kleidi/kleidiai
cmake -DCMAKE_BUILD_TYPE=Release -S . -B build/
cmake --build ./build
```
