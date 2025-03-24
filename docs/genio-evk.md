---
layout: default
title: Genio Evaluation Kits
nav_order: 2
---

# How to Install Your Genio Board?
##### update : 2025/01 by ITRI (EOSL-R3)

<div align="center">
<img src="assets/images/pages/genio_510_evk.png" width="560"/>
</div>

The Genio Evaluation Kits are designed to provide developers with a robust platform for **Computer Vision** and **AIoT** applications. These kits support both Yocto and Ubuntu 22.04 operating systems, each offering unique advantages to cater to different development needs.


### Operating Systems:

* **Yocto**: Known for its high power performance, Yocto is ideal for developers who require a highly customizable and efficient OS. However, it may present a steeper learning curve due to its complexity.
* **Ubuntu 22.04**: This OS is more user-friendly and easier to develop on, making it suitable for developers who prioritize ease of use and rapid development.


### Device Tpye: 

|  Devices     | Genio 510     | Genio 700     | Genio 1200     |
| :----------: |:-------------:|:-------------:|:--------------:|
| **OS**            |  `Yocto`, `Ubuntu 22.04`            |   `Yocto`, `Ubuntu 22.04`            |   `Yocto`, `Ubuntu 22.04`            |
| **CPU**           |  `Cortex-A55`x4,`Cortex-A78`x2      |   `Cortex-A55`x6,`Cortex-A78`x2      |   `Cortex-A55`x4,`Cortex-A78`x4      |
| **GPU**           |  `Mali-G57 MC2`                       |   `Mali-G57 MC3`                   |   `Mali-G57 MC5`                     |
| **APU**           | `MDLA 3.0`x1, `VP`x1                |   `MDLA 3.0`x1, `VP`x1               |   `MDLA 2.0`x2, `VP`x2               |
| **Performance**   | 0.15~2.8TOPs                        | 0.20~4.0TOPs                         | 0.25~4.8TOPs                         |
| **Power**         | 3.5~4.5W                            | 5~6W                                 | 6.2~7.2W                             |
| **Memory**        | 4GB LPDDR4                          | 8GB LPDDR4                           | 16GB LPDDR5                          |

Genio 510/700 are suitable for tasks with a single model and more complex structures (e.g., YOLO object detection). Among them, the 700 version has larger memory, which can accommodate higher computational power for streaming needs. On the other hand, the 1200 is suitable for tasks with composite models but simpler structures (e.g., ResNet image classification). You can choose the appropriate chipset according to your needs.

## AI Development Resources

The diverse chipset of this system provides extensive application potential, while also indicating that software developers will face a more complex development environment.

The diagram below illustrates the complete system resources and workflow. The workstation is used for installing the operating system on board and compiling trained models, all to enable efficient inference execution on the development board. The blue section represents the Arm CPU and Arm GPU, which can directly handle any model inference through TFLite delegation, though each inference will consume a significant amount of memory. The yellow section represents the MediaTek NPUs, which require further conversion of TFLite models to DLA format using the NeuronPilot tool. The Genio-510/700 features `mdla3.0` and `vpu`, while the Genio-1200 features `mdla2.0` and `vpu`. They support only a limited and different set of operators. You can use the [NeuronPilot Online](https://app-aihub-neuronpilot.azurewebsites.net/) tool to convert your custom model and check if it is supported.

<div align="center">
<img src="assets/images/pages/genio_510_demonstration_workflow.png" width="780"/>
</div>

Additionally, once the board is properly set up, you can perform model inference using Native Frameworks, ArmNN, or NeuronRT, each of which utilizes different computational resources. You can quickly set up these two environments by following the guidelines in the rest of this document. **Native Frameworks (TFLite)** primarily relies on the CPU for inference. **ArmNN** can accelerate inference by optimizing both the CPU and GPU, resulting in faster and more efficient processing compared to running inference without ArmNN. **NeuronRT** leverages the MediaTek Deep Learning Accelerator (MDLA) or Vision Processor (VP) for high-performance inference. For practical examples, please refer to the [Model Zoo](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo).

### References

1. [Get Started with IoT Yocto](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/get-started.html)
2. [Get Started with Ubuntu on Genio](https://mediatek.gitlab.io/genio/doc/ubuntu/get-started.html)

<br>
<div align="right">
<a href="https://r300-ai.github.io/ITRI-AI-Hub/docs/genio-evk/step1.html"> 

[ Next >> Step1. Setup Tools ]
  
</a>
</div>
