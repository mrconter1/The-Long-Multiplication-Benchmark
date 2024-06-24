import random
import asyncio
import re
import os

# List of models to benchmark
models_to_benchmark = [
    {"provider": "openai", "name": "gpt-3.5-turbo"},
    {"provider": "openai", "name": "gpt-4-turbo"},
    {"provider": "openai", "name": "gpt-4o"},
    {"provider": "google", "name": "gemini-1.5-pro"},
    {"provider": "anthropic", "name": "claude-3-5-sonnet-20240620"}
]

# Global variables
evaluations_per_length = 25
max_length = 7
openai_api_key = os.getenv('OPENAI_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')

# OpenAI setup
from openai import AsyncOpenAI
openai_client = AsyncOpenAI(api_key=openai_api_key)

# Google setup
import google.generativeai as genai
genai.configure(api_key=google_api_key)

# Anthropic setup
import anthropic
anthropic_client = anthropic.Anthropic(api_key=anthropic_api_key)

def generate_long_multiplication_question(length):
    A = random.randint(10**(length-1), 10**length - 1)
    B = random.randint(10**(length-1), 10**length - 1)
    C = A * B
    
    question = f"""think step by step, including for the sum of all the partial products (add them one by one): please multiply {A} and {B}
            MAKE SURE TO ANSWER IN THE FOLLOWING FORMAT BELOW:
            If the result is 43421, write 'Answer: 43421'
            If the result is 7623, write 'Answer: 7623'
            """

    return question, C

async def ask_model(question, model):
    try:
        if model["provider"] == "openai":
            response = await openai_client.chat.completions.create(
                model=model["name"],
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question}
                ],
                temperature=0.5
            )
            answer = response.choices[0].message.content.strip()
        elif model["provider"] == "google":
            google_model = genai.GenerativeModel(model["name"])
            response = google_model.generate_content(question)
            answer = response.text.strip()
        elif model["provider"] == "anthropic":
            response = anthropic_client.messages.create(
                model=model["name"],
                max_tokens=4000,
                temperature=0.5,
                messages=[
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )
            answer = response.content[0].text
        return answer
    except Exception as e:
        print(f"Error during API call: {e}")
        return None

async def benchmark_model(model, evaluations_per_length, max_length):
    results = {}
    print(f"Evaluating model: {model['name']}")

    for length in range(1, max_length + 1):
        correct = 0
        tasks = []

        for _ in range(evaluations_per_length):
            question, correct_answer = generate_long_multiplication_question(length)
            tasks.append((question, correct_answer))

        responses = await asyncio.gather(*[ask_model(q, model) for q, _ in tasks])

        for (question, correct_answer), model_answer in zip(tasks, responses):
            question_str = question.split("of ")[-1].split(" to")[0]
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

        success_rate = (correct / evaluations_per_length) * 100
        results[length] = success_rate
        print(f"Success Rate for length {length}: {success_rate:.2f}%\n")

    return model["name"], results


async def main():
    all_results = {}
    for model in models_to_benchmark:
        model_name, results = await benchmark_model(model, evaluations_per_length, max_length)
        all_results[model_name] = results

    # Generating the final results table
    print("\nFinal Results:")
    lengths = list(range(1, max_length + 1))
    headers = ["Length"] + [model["name"] for model in models_to_benchmark]
    table = []

    for length in lengths:
        row = [length]
        for model in models_to_benchmark:
            model_name = model["name"]
            row.append(f"{all_results[model_name][length]:.2f}")
        table.append(row)

    # Print the table
    print("| " + " | ".join(headers) + " |")
    print("| " + " | ".join(["--------"] * len(headers)) + " |")
    for row in table:
        print("| " + " | ".join(map(str, row)) + " |")

if __name__ == "__main__":
    asyncio.run(main())