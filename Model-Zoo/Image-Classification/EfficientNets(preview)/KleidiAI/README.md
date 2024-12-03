# Deploy EfficientNets on Kleidi AI
### Prerequisites

* Any **EfficientNet** model in `ONNX` format obtained from [[Training/Performance Evaluation]](https://github.com/R300-AI/ITRI-AI-Hub/tree/main/Model-Zoo/Object-Detection/RT-DETR(preview)) part.
* An **Arm Processors Board** with **Kleidi AI** Library installed. ([[Installation Guide]](https://r300-ai.github.io/ITRI-AI-Hub/docs/pages/runtime/kleidi.html))

## Deploy Sample Codes on Board

**Step 1.** Install dependencies on your board.

```bash
$ pip install -r requirements.txt
```

**Step 2.** Execute an detection for `./bus.jpg`.

```bash
$ python run.py --model_path <path_to_your_model>.onnx
```
