---
layout: default
title: Quick Start
nav_order: 1
---

# Get Started
##### update : 2025/01 by ITRI(EOSL-R3)

工研院AI Hub為企業及開發者提供簡單、快速、商業化的Edge AI實施方案。在選擇系統之前，我們建議您依照運算能力及能源效率來評估哪些設備適合您所設計的應用。

<br>ITRI AI Hub offers simple, fast, and commercialized Edge AI implementation solutions for enterprises and developers. Before selecting a system, we recommend evaluating which devices are suitable for your designed applications based on computing power and energy efficiency.

<div align="center"><img src="../assets/images/software-support-metric.png" width="840"/></div>


# Get Started
##### update : 2024/11 by Markov Chen

<br>Before selecting an embedded processor for your application, we recommend that you review the use cases or similar real-world models in Model Zoo. Then, select the appropriate Evaluation Kits based on their performance benchmarks on different processors. (...增加下圖的描述)

<div align="center"><img src="../assets/images/software-support-metric.png" width="840"/></div>

In the following documents, we provide software installation guidelines for Work Stations and Evaluation Kits to meet the basic needs of developing embedded AI:

* **Work Station**: This term refers to the host used to develop and train AI models (usually through PyTorch or TensorFlow), which mainly includes facilities such as GPUs and CPUs. Typically, it is separate from embedded systems because this stage requires high performance and high power consumption.
    > **Converter Tools**: These tools involve vendor-specific properties designed to translate the model into instructions readable by the embedded processors.

* **Evaluation Kits**: This term refers to lightweight motherboards designed specifically for certain embedded processors. Due to their highly reconfigurable hardware, they are often used in the development of various portable devices and electronic products.
    > **Runtime APIs**: APIs that delegate the model inference process to designated computing units. Usage examples can be found in the Model Zoo.


# Welcome to ITRI AI Hub Document

<p>
<div style="margin-left: 20px;">
The ITRI AI Hub provides a comprehensive AI infrastructure solution to help enterprises construct a portable AI system with <b>Compliant, Secure,</b> and <b>High Energy Efficiency</b>. Developers can find the optimal computing units on this platform for implementing various sophisticated applications.
</div>
</p>

<div style="margin-left: 20px;">
<br>Imagine how important an Embedded AI with high durability is in a jungle with no internet connection. Let's suppose you're alone with your digital assistant, but unable to use its full functionality due to no internet connectivity. Embedded AI is able to efficiently process data and perform tasks on a local device, meaning that even when the internet is unavailable, your digital assistant can still identify dangerous animals and plants, provide voice survival guides, and monitor physiological conditions, among other key functions. A laptop workstation is an alternative solution. however, it may face challenges such as limited battery life. In contrast, using cloud-based AI involves bottlenecks such as finding network signals, connecting to the network, synchronizing data and requesting cloud services, all of which may not be completed in real-time during such emergencies, thereby compromising your safety and convenience.
</div>

## **Designed for AI Applications Everywhere**

<div style="margin-left: 20px;">
<br>This statement does not undermine the necessity of cloud computing and computational workstations; however, it acknowledges that embedded AI can be more reliable and energy-efficient in commercial scenarios. As the examples shown below, our AI application services cover a wide range of functions in different domains, including <b>vision, voice/signal, language</b>, and <b>processing and optimization</b>. In computer vision, we provide advanced image classification, object detection, character recognition and keypoint identification functions. These functions enable precise analysis and interpretation of image data. In speech and signal processing, we provide powerful text-to-speech, speech-to-text and time-series analysis functions. These services contribute to effective communication and signal processing. In the language domain, our AI services include sophisticated text understanding, entity extraction and question answering systems. These features enhance natural language understanding and interaction. In the processing and optimization area, dynamic planning, enhanced learning control and search engines are featured. These functions are designed to improve operational efficiency and decision-making processes.
</div><br>

<div align="center"><img src="./assets/images/tasks.png" width="720"/></div>
(待修正為1. Vision 2. Voice/ Signal 3. Language 4. Processing and Optimization四項)

## **What Can We Do?**

<div style="margin-left: 20px;">
It is imperative that we thoroughly understand the entire application environment and define the basic requirements of each functional unit, to determine where each microservice in the system should be delegated and the carriers. Furthermore, we are committed to integrating the latest embedded hardware solutions and conducting feasibility assessments for porting these functions. Our comprehensive reports will enable organizations to swiftly implement these advanced AI options into their systems, ensuring that private data remains close to the client host. Therefore, we build the AI Hub to help enterprises find more rational use of computing costs and resources. The following figure roughly shows the currently supported edge system inference benchmarks. These results are achieved through the engines of each major processor. You can evaluate whether these edge devices are suitable for your system configuration based on the underlying transfer efficiency, power consumption and computing speed.
</div><br>

<div align="center"><img src="./assets/images/metric.png" width="720"/></div>
<br>
<div align="right"><a href="https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/get-started.html"> >> Next: Get Started</a></div>
