---
layout: default
title: "　-　KleidiAI"
nav_order: 31
---

# Arm Kleidi AI
##### update : 2024/10 by Markov Chen
<br>

Arm KleidiAI is a specialized library designed to enhance the performance of AI frameworks on Arm CPUs. It provides optimized micro-kernels that leverage the unique architecture of Arm processors, enabling more efficient execution of AI workloads. By integrating KleidiAI into your AI projects, you can achieve significant improvements in computational speed and resource utilization, making it an essential tool for developers working with AI on Arm-based systems.

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
