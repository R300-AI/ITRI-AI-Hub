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
ollama run smollm2:135m "Gravity is" --verbose

# >> Gravity. A fundamental concept in physics that has puzzled mathematicians and physicists for centuries. It arises from the way objects fall towards the ground due to gravity. However, it's fascinating to note that gravitational mass doesn't exactly depend on its density or composition - a subtle difference between gravity and inertia can arise.
```
```bash
ollama run qwen2.5:0.5b "Give me a short introduction to large language model." --verbose

# >> Certainly! A large language model (LLM) is a type of artificial intelligence system designed and trained using deep learning algorithms. These models can generate human-like text and perform specific tasks such as translation, summarization, machine translation, and more.
```
```bash
ollama run llama3.2:1b "The key to life is" --verbose

# >> It sounds like you're about to share something interesting. The phrase "The key to life" can refer to various things, and I'm curious - what are your thoughts on it? Are you looking for inspiration, wisdom, or perhaps a specific insight that will help guide you through life's journey?
```
