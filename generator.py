"""
StudyGen AI
Question Generator using Hugging Face Inference API
"""

import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from prompts import build_prompt
from utils import clean_text

# ----------------------------------------------------
# Load environment variables
# ----------------------------------------------------

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "Qwen/Qwen2.5-7B-Instruct"
)

if not HF_TOKEN:
    raise ValueError(
        "HF_TOKEN not found. Please create a .env file."
    )

print("Connecting to Hugging Face Inference API...")

client = InferenceClient(
    api_key=HF_TOKEN,
)

print("Connected successfully!")

# ----------------------------------------------------
# Generate Questions
# ----------------------------------------------------


def generate_questions(
    text,
    question_type,
    difficulty,
    number,
):
    """
    Generate study questions from supplied notes.
    """

    if not text or not text.strip():
        return "No study material was provided."

    # Clean the notes
    text = clean_text(text)

    # Build the AI prompt
    prompt = build_prompt(
        text=text,
        question_type=question_type,
        difficulty=difficulty,
        number=number,
    )

    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert university lecturer and assessment designer. "
                "Generate high-quality revision questions based ONLY on the notes "
                "provided by the user. Do not invent facts that are not present "
                "in the notes."
            ),
        },
        {
            "role": "user",
            "content": prompt,
        },
    ]

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            max_tokens=1200,
            temperature=0.7,
        )

        if (
            response.choices
            and response.choices[0].message.content
        ):
            return response.choices[0].message.content.strip()

        return "The AI returned an empty response."

    except Exception as e:

        return (
            "An error occurred while generating questions.\n\n"
            f"{str(e)}"
        )


# ----------------------------------------------------
# Local Test
# ----------------------------------------------------

if __name__ == "__main__":

    sample = """
Artificial Intelligence (AI) is the simulation of human intelligence by machines.

Machine Learning is a subset of Artificial Intelligence.

Deep Learning is a subset of Machine Learning.

Supervised learning uses labelled data.

Unsupervised learning discovers hidden patterns in data.

Reinforcement learning trains agents using rewards and penalties.
"""

    print("\nGenerating questions...\n")

    result = generate_questions(
        text=sample,
        question_type="Multiple Choice",
        difficulty="Medium",
        number=5,
    )

    print(result)