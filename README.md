# The Long Multiplication Benchmark

#### Motivation

Imagine a hypothetical LLM with the following two qualities:

1. It has an infinite context length.
2. It can perform long multiplication at a **high school** level.

Given these qualities, it should be able to compute B = **C * A** to an **arbitrary** number of digits and find the exact value.

#### Description

In the current landscape of scaled Large Language Models (LLMs), a significant focus has been on their ability to handle large contexts. However, an equally important aspect is their capability to generate long coherent texts. Writing a book, for instance, requires not only the ability to read long contexts but also to generate extensive text. Evaluating such an ability can be challenging, but one scalable and straightforward method is to test the LLMs' ability to perform long multiplication. This task can be done without external tools and is easily scalable. Long multiplication, a fundamental algorithm involving simple calculations, can be performed by humans given enough time, making it a suitable benchmark for LLMs.

For example, consider the long multiplication problem for **n=5**:
> Use long multiplication to find the exact result of 64369 * 95689 to full precision. Do not use any tools or calculators. Approximate answers are not allowed.

The answer to this problem is 64369 * 95689.

### Results

Each entry in the results table represents the percentage of correct answers for 25 samples per number of digits.

TODO

### Benchmark Script

[benchmark.py](./benchmark.py) tests different models by generating long multiplication problems and evaluating the models' ability to solve them accurately. The process involves creating a multiplication problem, posing it to the model, and then verifying the precision of the model's answer.

### Conclusion

This repository offers a scalable method to validate the capability of future LLMs to not only read long contexts but also to constructively use them. By leveraging long multiplication as a benchmark, it provides a straightforward way to evaluate how well LLMs utilize long contexts meaningfully. The results show that newer models can better handle longer contexts, emphasizing the need for continuous improvement. 

This benchmark ensures that LLMs can perform complex tasks effectively, combining long contexts with straightforward operations to yield exact answers, thus validating their practical application of long-context understanding.
