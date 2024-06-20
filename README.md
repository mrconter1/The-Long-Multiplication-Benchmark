# The Long Multiplication Benchmark

The Long Multiplication Benchmark evaluates Large Language Models (LLMs) on their ability to handle and utilize extensive contexts by solving long multiplication problems. Despite having sufficient context sizes and computational resources, current LLMs struggle to effectively use the information within their context windows, highlighting a **serious limitation** in their ability to actually use their context window.

#### Motivation

Imagine a hypothetical LLM with the following premises:

1. It is capable of performing schoolbook long multiplication.
2. It can **perfectly** utilize information within its context window.
3. It has the necessary computational resources.

Given these premises, the context length should be the **only** limiting factor in determining how large numbers it can calculate.

#### Description

In the current landscape of scaled Large Language Models (LLMs), a significant focus has been on their ability to handle large contexts. However, an equally important aspect is their capability to generate long coherent texts. Writing a book, for instance, requires not only the ability to read long contexts but also to generate extensive text. Evaluating such an ability can be challenging, but one scalable and straightforward method is to test the LLMs' ability to perform long multiplication. This task can be done without external tools and is easily scalable. Long multiplication is akin to executing an algorithm like a computer, involving precise steps without the need for estimations, making it a more straightforward benchmark compared to tasks like long division, which require estimation steps, as seen in benchmarks like [The Long Division Benchmark](https://github.com/mrconter1/The-Long-Division-Benchmark/).

For example, consider the long multiplication problem for **n=5**:
> Use the schoolbook method to find the exact result of 64369 * 95689. Show all steps and carried digits. Do not use any tools or calculators. Perform all calculations thoroughly and exactly.

The answer to this problem is 6159405241.

*Note: This is a simplified version of the prompt. The full prompt can be found in the benchmark.*

### Results

Each entry in the results table represents the percentage of correct answers for 25 samples per number of digits. The context window size for each model is also provided.

| Length | gpt-3.5-turbo (16K tokens) | gpt-4-turbo (128K tokens) | gpt-4o (128K tokens) | gemini-1.5-pro (1M tokens) |
|--------|-----------------------------|---------------------------|----------------------|----------------------------|
| 1      | 100.00                      | 100.00                    | 100.00               | 100.00                     |
| 2      | 96.00                       | 100.00                    | 100.00               | 100.00                     |
| 3      | 48.00                       | 64.00                     | 64.00                | 56.00                      |
| 4      | 4.00                        | 12.00                     | 12.00                | 20.00                      |
| 5      | 0.00                        | 0.00                      | 0.00                 | 0.00                       |
| 6      | 0.00                        | 0.00                      | 0.00                 | 0.00                       |
| 7      | 0.00                        | 0.00                      | 0.00                 | 0.00                       |

### Benchmark Script

[benchmark.py](./benchmark.py) tests different models by generating long multiplication problems and evaluating the models' ability to solve them accurately. The process involves creating a multiplication problem, posing it to the model, and then verifying the precision of the model's answer.

### Conclusion

The benchmark demonstrates that while the context sizes and computational resources of current LLMs are theoretically sufficient, the limiting factor is their inability to actually utilize the information within their context windows efficiently.

This repository offers a scalable method to validate the capability of future LLMs to not only read long contexts but also to constructively use them. By leveraging long multiplication as a benchmark, it provides a straightforward way to evaluate how well LLMs utilize long contexts meaningfully.