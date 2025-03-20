<div align="center">
  
  [ITRI AI Hub](https://e-aihub.dev/) is an **AI Deployment Verification Platform** build upon selected CPUs, GPUs, MCUs, and DLAs. It is designed to delegate the computer vision (CV), natural language process (NLP), audio signals and multimodal models to be accelerated on-chip. making AI application proof-of-concept and commercial implementation easier.

Contact With Us :wave:

| [Application Validation](mailto:sylvia.chan@itri.org.tw) | [Chipset Partnership](mailto:Markv.chen1996@itri.org.tw) | [Developer Support](mailto:Markv.chen1996@itri.org.tw) |

</div>

## <div align="center">Documentations</div>

<details>
<summary>Arm Raspberry Pi Module</summary>
</details>

<details open>
<summary>MediaTek Genio AIoT Module</summary>

Genio is powered by **Arm Cortex-A**, **Arm GPU** and **MediaTek DLA**, providing 0.3~4.8 FTOPS of low-power AI computing performance. It supports General-Purpose I/O (GPIO) interfaces, making it suitable for developing AIoT-level computer vision applications.

![](https://img.shields.io/badge/OS-Ubuntu_|_Yocto-orange) ![](https://img.shields.io/badge/NeuronPilot-v6-blue) ![](https://img.shields.io/badge/Python-3.7-green)
  * [Get Started with IoT Yocto](https://mediatek.gitlab.io/aiot/doc/aiot-dev-guide/master/sw/yocto/get-started.html)
  * [Get Started with Ubuntu on Genio](https://mediatek.gitlab.io/genio/doc/ubuntu/get-started.html)
  * [Deploy Pre-Trained Models using NVIDIA TAO Toolkit](https://mediatek.gitlab.io/genio/doc/tao/index.html)

</details>

<details>
<summary>AMD Ryzen AI PC Module</summary>

AMD Ryzen AI processors are SoCs specifically designed for AI PCs, integrating the most powerful **Zen CPU** and **RDNA GPU**, capable of delivering up to 50 TOPs of AI performance.

![](https://img.shields.io/badge/OS-Windows-orange) ![](https://img.shields.io/badge/Quark_Quantizer-latest-blue) ![](https://img.shields.io/badge/Vitis_AI_EP-latest-blue) ![](https://img.shields.io/badge/Python->3.6-green)
  * [Development Flow Overview](https://ryzenai.docs.amd.com/en/latest/index.html)
  * [Examples, Demos, Tutorials for Ryzen AI Software](https://ryzenai.docs.amd.com/en/latest/examples.html)
  * [AMD Quark Quantizer for Efficient AI Model Deployment](https://www.amd.com/en/developer/resources/technical-articles/amd-quark-quantizer-for-efficient-ai-model-deployment.html)

</details>

<details>
<summary>NVIDIA Jetson GPU Module</summary>
  
Jetson Orin is a cutting-edge SoC tailored for edge AI applications, featuring an **Arm CPU** and the most powerful **Ampere GPUs**. It delivers impressive AI performance ranging from 67~275 TOPS.

![](https://img.shields.io/badge/OS-Ubuntu_|_JetPack-orange) ![](https://img.shields.io/badge/TensorRT-latest-blue) ![](https://img.shields.io/badge/Python->3.6-green)

</details>

<details>
<summary>WiseEye2 AI Processor</summary>

Ethos U55 NPU
 
</details>

<details>
<summary>Hailo AI Processor</summary>

Hailo offers 26~40 TOPs expansion cards designed for accelerating computer vision process. It provide **mPCIe/M.2 interface** to connect with above modules. **(*registration is required to access the documents)**

![](https://img.shields.io/badge/Data_Compiler-3.27.0-blue) ![](https://img.shields.io/badge/PyHailoRT-4.17-blue) ![](https://img.shields.io/badge/Python-3.8-green)
  * [Install Dataflow Compiler with Evaluation Board](https://hailo.ai/developer-zone/documentation/dataflow-compiler-v3-27-0/?sp_referrer=install/install.html)
  * [Install HailoRT(PCIe Driver) and pyHailoRT with mPCIe or M.2 board](https://hailo.ai/developer-zone/documentation/hailort-v4-17-0/?sp_referrer=install/install.html#ubuntu-installer-requirements)
</details>


<table>
    <tr>
        <th>Category</th>
        <th>Application</th>
        <th>Pi<br>
        <th>Genio<br>
        <th>Ryzen</th>
        <th>Jetson</th>
        <th>WE</th>
        <th>Hailo</th>
    </tr>
    <tr>
        <td rowspan=3>CV</td>
        <td>Image Classification</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
    </tr>
    <tr>
        <td>Object Detection</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
    </tr>
    <tr>
        <td>Semantic Segmentation</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
    </tr>
    <tr>
        <td rowspan=1>NLP</td>
        <td>Text to Text</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:black_square_button:</td>
        <td>:black_square_button:</td>
    </tr>
    <tr>
        <td rowspan=1>Voice Signals</td>
        <td>Speech-Recognition</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:black_square_button:</td>
        <td>:black_square_button:</td>
    </tr>
    <tr>
        <td rowspan=2>Multi Modal</td>
        <td>Text to Image</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:black_square_button:</td>
        <td>:black_square_button:</td>
    </tr>
    <tr>
        <td>Text to Voice</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:white_check_mark:</td>
        <td>:black_square_button:</td>
        <td>:black_square_button:</td>
    </tr>
</table>

## <div align="center">News</div>

* 2024/09 Released a Simple and Clear **Developer's Tutorial** Website [HERE](https://r300-ai.github.io/ITRI-AI-Hub/).
* 2024/07 Started Testing Model Deployment with **NVIDIA, AMD, ARM,** and **Mediatek**.
* 2024/05 Release **ITRI AI Hub**.
  
## <div align="center">Contridutors</div>

<a href="https://www.moea.gov.tw/Mns/populace/home/Home.aspx" target="AI晶片異質整合模組前瞻製造平台計畫"><img src="https://github.com/R300-AI/ITRI-AI-Hub/blob/main/docs/assets/images/logo/moea_logo.png" alt="MOEA logo" height="38" width="216"></a>&nbsp;
<a href="https://www.itri.org.tw/index.aspx" target="工業技術研究院"><img src="https://github.com/R300-AI/ITRI-AI-Hub/blob/main/docs/assets/images/logo/itri_EL_A.jpg" alt="ITRI logo" height="39"></a>&nbsp;
<a href="https://www.amd.com/zh-tw.html" target="amd"><img src="https://github.com/R300-AI/ITRI-AI-Hub/blob/main/docs/assets/images/logo/amd_logo.png" alt="amd logo" height="33"></a>&nbsp;&nbsp;&nbsp;
<a href="https://www.arm.com/zh-TW/" target="Arm"><img src="https://github.com/R300-AI/ITRI-AI-Hub/blob/main/docs/assets/images/logo/arm_logo.png" alt="Arm logo" height="33"></a>&nbsp;&nbsp;
<a href="https://www-stage.mediatek.com/zh-tw/" target="聯發科技"><img src="https://github.com/R300-AI/ITRI-AI-Hub/blob/main/docs/assets/images/logo/mediatek_logo.png" alt="MediaTek logo" height="35"></a>&nbsp;


## <div align="center">License</div>

