# About Ollama
# Benchmarks
## Inference/Performance Evaluation

|  Model         | Size        |  Dataset               | Context<br> Length|  Metric           |
|----------------|-------------|------------------------|-------------------|-------------------|
| smollm2:135m   |270 MB  | Public online data.    |                   | `MMLU(31.5)`      |
| smollm2:360m   |726 MB  | Public online data.    |                   | `MMLU(35.8)`      |
| smollm2:1.7b   |1.8 GB  | Public online data.    |                   | `MMLU-Pro(19.3)`  |
| llama3.2:1b    |1.23B   | Public online data.    | 128k              | `MMLU(32.2)`      |
| llama3.2:3b    |3.21B   | Public online data.    | 128k              | `MMLU(58.0)`      |
| qwen2.5:0.5b   |397 MB  | Textbook data.         | 128k              | `MMLU(45.4)`      |
| qwen2.5:1.5b   |986 MB  | Textbook data.         | 128k              | `MMLU(56.5)`      |
| qwen2.5:3b     |1.9 GB  | Textbook data.         | 128k              | `MMLU(63.2)`      |
| qwen2.5:7b     |4.7 GB  | Textbook data.         | 128k              | `MMLU(70.3)`      |
| phi3.5         |2.2 GB  | Textbook data.         | 128k              | `MMLU(69.0)`      |
| phi3           |2.2 GB  | Textbook data.         | 128k              | `MMLU(55.4)`      |


```bash
curl -fsSL https://ollama.com/install.sh | sh
```
