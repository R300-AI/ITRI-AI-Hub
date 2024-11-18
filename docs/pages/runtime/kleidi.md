---
layout: default
title: "　-　KleidiAI"
nav_order: 41
---

# Install Arm Kleidi AI for ARM64 Boards
##### update : 2024/10 by Markov Chen
<br>

KleidiAI is a universal AI acceleration platform that supports a wide range of AI accelerator hardware. It provides a rich set of APIs and tools that allow developers to easily deploy deep learning models to different hardware. KleidiAI supports leading deep learning frameworks such as TensorFlow, PyTorch, and ONNX, and is able to automatically optimise the model inference process to improve performance and efficiency. This makes KleidiAI a flexible and powerful solution for a variety of AI application scenarios.

### Prerequisites
* To install Kleidi AI, your board must contain with arm64 processor.

## Installation

### Step 1: Build the Kleidi AI Library
To build the Kleidi library on your system, execute the following commands:

```bash
$ cd && git clone https://gitlab.arm.com/kleidi/kleidiai && cd kleidiai
$ cmake -DCMAKE_BUILD_TYPE=Release -S . -B build/
$ cmake --build ./build
```

### Step 2: Build the Kleidi CV Library
To build the Kleidi library on your system, execute the following commands:
```bash
$ wget https://github.com/opencv/opencv/archive/refs/tags/4.10.0.tar.gz
$ tar xf 4.10.0.tar.gz
$ cd opencv-4.10.0
$ patch -p1 </path/to/kleidicv/adapters/opencv/opencv-4.10>.patch
```
```bash
$ https://git.gitlab.arm.com/kleidi/kleidicv.git
$ cmake -S </path/to/opencv> -B build-opencv-linux -DWITH_KLEIDICV=ON -DKLEIDICV_SOURCE_PATH=</path/to/kleidicv>
$ cmake --build build-opencv-linux --parallel
```

## Appendix

* [Arm blog: KleidiAI Helping AI frameworks elevate their performance on Arm CPUs](https://community.arm.com/arm-community-blogs/b/ai-and-ml-blog/posts/kleidiai)
* [KleidiAI Gitlab - micro-kernels for Arm® CPUs](https://gitlab.arm.com/kleidi/kleidiai)
* [KleidiCV Gitlab - micro-kernels for Arm® GPUs](https://gitlab.arm.com/kleidi/kleidicv)
