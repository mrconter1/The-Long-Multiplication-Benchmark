import asyncio
import re
import backend

evaluations_per_template = 5
max_length = 9

models_to_benchmark = [
    {"provider": "openai", "name": "gpt-3.5-turbo"},
    {"provider": "openai", "name": "gpt-4-turbo"},
    {"provider": "openai", "name": "gpt-4o"},
    {"provider": "google", "name": "gemini-1.5-pro"},
    {"provider": "anthropic", "name": "claude-3-5-sonnet-20240620"}
]

async def benchmark_model(model, evaluations_per_template, max_length):
    results = {}
    print(f"Evaluating model: {model['name']}")

    # Load templates
    multiplication_templates = backend.load_question_templates()

    for length in range(1, max_length + 1):
        correct = 0
        tasks = []

        for template in multiplication_templates:
            for _ in range(evaluations_per_template):
                question, correct_answer = backend.generate_long_multiplication_question(length, template['template'])
                tasks.append((question, correct_answer))

        responses = await asyncio.gather(*[backend.ask_model(q, model) for q, _ in tasks])

        for (question, correct_answer), model_answer in zip(tasks, responses):
            question_str = question.split("multiply ")[-1].split("\n")[0]
            print(f"Problem: {question_str}")
            print(f"Expected Answer: {correct_answer}")

            if model_answer:
                try:
                    # Use regex to find the answer in the model's response
                    answer_match = re.search(r'.*Answer.*?([\d]+)', model_answer, re.DOTALL)
                    if answer_match:
                        parsed_answer = int(answer_match.group(1))
                        print(f"Given Answer: {parsed_answer}")
                        if parsed_answer == correct_answer:
                            correct += 1
                            print("Result: Correct\n")
                        else:
                            print("Result: Incorrect\n")
                    else:
                        print("Result: No valid answer found\n")
                        print(model_answer)
                except ValueError:
                    print("Result: Error in parsing model answer\n")
                    print(model_answer)
            else:
                print("Result: No response from model\n")

        success_rate = (correct / (evaluations_per_template * len(multiplication_templates))) * 100
        results[length] = success_rate
        print(f"Success Rate for length {length}: {success_rate:.2f}%\n")

    return model["name"], results

async def run_benchmark(models_to_benchmark, evaluations_per_template, max_length):
    all_results = {}
    for model in models_to_benchmark:
        model_name, results = await benchmark_model(model, evaluations_per_template, max_length)
        all_results[model_name] = results
    return all_results

def print_benchmark_results(all_results, max_length):
    # Generating the final results table
    print("\nFinal Results:")
    lengths = list(range(1, max_length + 1))
    headers = ["Length"] + list(all_results.keys())
    table = []

    for length in lengths:
        row = [length]
        for model_name in all_results.keys():
            row.append(f"{all_results[model_name][length]:.2f}")
        table.append(row)

    # Print the table
    print("| " + " | ".join(headers) + " |")
    print("| " + " | ".join(["--------"] * len(headers)) + " |")
    for row in table:
        print("| " + " | ".join(map(str, row)) + " |")

async def main():
    all_results = await run_benchmark(models_to_benchmark, evaluations_per_template, max_length)
    print_benchmark_results(all_results, max_length)

if __name__ == "__main__":
    asyncio.run(main())