"""
StudyGen AI
Question Generator using Hugging Face Inference API
"""

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from generator import generate_questions

from prompts import build_prompt
from utils import clean_text

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-7B-Instruct")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN not found. Please create a .env file.")

print("Connecting to Hugging Face Inference API...")

client = InferenceClient(
    api_key=HF_TOKEN
)

print("Connected successfully!")


def generate_questions(
    text,
    question_type,
    difficulty,
    number
):
    """
    Generate study questions using Hugging Face Inference API.
    """

    text = clean_text(text)

    prompt = build_prompt(
        text=text,
        question_type=question_type,
        difficulty=difficulty,
        number=number
    )

    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert university lecturer who creates "
                "high-quality revision questions."
            ),
        },
        {
            "role": "user",
            "content": prompt,
        },
    ]

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        max_tokens=1200,
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()
