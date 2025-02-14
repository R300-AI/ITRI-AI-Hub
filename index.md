---
layout: default
title: Quick Start
nav_order: 1
---

# Welcome to ITRI AI Hub Tutorials
##### update : 2025/01 by ITRI (EOSL-R3)

<br>ITRI AI Hub offers simple, fast, and commercialized Edge AI implementation solutions for enterprises and developers. Before selecting a system, we recommend evaluating which devices are suitable for your applications based on model type, computing power, memory, and energy efficiency. The diagram below summarizes the memory and computing power distribution of devices we selected, helping you compare them more intuitively with Model Zoo, open-source communities, or other custom models.

<div align="center"><img src="./docs/assets/images/pages/metric_of_all_devices.png" width="760"/></div>


## **Development Flow Overview**

<div style="margin-left: 20px;">
<br>

Overall, a model deployment process involves three stages: training, compilation, and inference.


<ul>
  <li><strong>Training</strong>: This term refers to the phase where AI models are developed and trained (typically using PyTorch or TensorFlow) on a host machine.
    <ul>
      <li><a href="https://azure.microsoft.com/zh-tw">Azure-hosted cloud</a></li>
      <li><a href="https://www.amd.com/zh-tw/products/software/rocm.html">Servers or Workstations with ROCm</a></li>
      <li><a href="https://developer.nvidia.com/cuda-toolkit">Servers or Workstations with CUDA</a></li>
    </ul>
  </li>
  <li><strong>Compiling</strong>: These tools involve vendor-specific attributes designed to convert models into instructions readable by embedded processors.</li>
  <li><strong>Inference</strong>: This term refers to lightweight host boards designed for specific embedded processors. 
    <ul>
      <li><a href="https://r300-ai.github.io/ITRI-AI-Hub/docs/genio-evk.html">Genio Evaluation Kits</a></li>
      <li><a href="https://r300-ai.github.io/ITRI-AI-Hub/docs/hailo.html">Hailo AI Accelerator</a></li>
      <li><a href="https://r300-ai.github.io/ITRI-AI-Hub/docs/ryzen.html">Ryzen AI Processor</a></li>
      <li><a href="https://r300-ai.github.io/ITRI-AI-Hub/docs/jetson-evk.html">Jetson Evaluation Kits</a></li>
    </ul>
  </li>
  <li><strong>Runtime API</strong>: APIs that delegate the model inference process to designated computational units. Examples of usage can be found in model zoos.</li>
</ul>

Visit "Developer Support" for more information
</div><br>


## **How to Build Your Own Application?**

* [Train Your Own Model]()
* [Pre-trained Model from Model Zoo or Third-Party]()