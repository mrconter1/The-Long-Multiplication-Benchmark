import random
import json
import os

# OpenAI setup
from openai import AsyncOpenAI
openai_api_key = os.getenv('OPENAI_API_KEY')
openai_client = AsyncOpenAI(api_key=openai_api_key)

# Google setup
import google.generativeai as genai
google_api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=google_api_key)

# Anthropic setup
import anthropic
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
anthropic_client = anthropic.Anthropic(api_key=anthropic_api_key)

def load_question_templates(file_path='question_templates.json'):
    with open(file_path, 'r') as file:
        templates = json.load(file)
    return templates

def generate_long_multiplication_question(length, template):
    A = random.randint(10**(length-1), 10**length - 1)
    B = random.randint(10**(length-1), 10**length - 1)
    C = A * B

    # Format the question using the provided template
    question = template.format(A=A, B=B)

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
            response = await anthropic_client.messages.create(
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