"""
StudyGen AI
Question Generator using Qwen2.5-1.5B-Instruct
"""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from prompts import build_prompt
from utils import clean_text


MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"

print("Loading Qwen model...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True
)

print("Model loaded successfully!")


def generate_questions(
    text,
    question_type,
    difficulty,
    number
):

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
            "content":
            "You are an expert university lecturer that creates high-quality study questions."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    prompt_text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(
        prompt_text,
        return_tensors="pt"
    ).to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=700,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.1,
        do_sample=True
    )

    generated = outputs[0][inputs.input_ids.shape[-1]:]

    return tokenizer.decode(
        generated,
        skip_special_tokens=True
    )