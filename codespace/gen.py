from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from codespace.prompt import build_prompt
import torch


MODEL_NAME = "google/flan-t5-small"

print("Loading model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

device = "cuda" if torch.cuda.is_available() else "cpu"

model.to(device)

print(f"Model loaded on {device}")


def generate_questions(
    text,
    question_type,
    difficulty,
    number
):
    """
    Generate study questions from the supplied material.
    """

    prompt = build_prompt(
        text=text,
        question_type=question_type,
        difficulty=difficulty,
        number=number
    )

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    inputs = {k: v.to(device) for k, v in inputs.items()}

    outputs = model.generate(
        **inputs,
        max_new_tokens=300,
        temperature=0.7,
        do_sample=True
    )

    return tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )
