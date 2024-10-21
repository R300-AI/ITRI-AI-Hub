---
layout: default
title: "　-　KleidiAI"
nav_order: 31
---

# Install Arm Kleidi AI for ARM64 System
##### update : 2024/10 by Markov Chen
<br>

KleidiAI is a universal AI acceleration platform that supports a wide range of AI accelerator hardware. It provides a rich set of APIs and tools that allow developers to easily deploy deep learning models to different hardware. KleidiAI supports leading deep learning frameworks such as TensorFlow, PyTorch, and ONNX, and is able to automatically optimise the model inference process to improve performance and efficiency. This makes KleidiAI a flexible and powerful solution for a variety of AI application scenarios.

## Installation

### Step 1: Build the Kleidi Library
To build the Kleidi library on your system, execute the following commands:

```bash
$ cd && git clone https://gitlab.arm.com/kleidi/kleidiai && cd kleidiai
$ cmake -DCMAKE_BUILD_TYPE=Release -S . -B build/
$ cmake --build ./build
```

## Appendix

* [Arm blog: KleidiAI Helping AI frameworks elevate their performance on Arm CPUs](https://community.arm.com/arm-community-blogs/b/ai-and-ml-blog/posts/kleidiai)
* [KleidiAI Gitlab - micro-kernels for Arm® CPUs](https://gitlab.arm.com/kleidi/kleidiai)
