---
layout: default
title: "　-　CUDA"
nav_order: 11
---

# 
```
sudo apt update
sudo apt upgrade

sudo ubuntu-drivers install nvidia:535
```
```
nvidia-smi
```
```
pip3 install torch torchvision torchaudio

python3 -c "import torch; print(torch.cuda.is_available())"
```
