"""
StudyGen AI
Prompt Builder

Builds prompts for Qwen2.5-Instruct.
"""


def build_prompt(text, question_type, difficulty, number):
    """
    Build an optimized prompt for Qwen.

    Args:
        text (str): Study material
        question_type (str): Short Answer, Multiple Choice,
                             True/False, Essay
        difficulty (str): Easy, Medium, Hard
        number (int): Number of questions

    Returns:
        str
    """

    question_type = question_type.strip().lower()

    if question_type == "multiple choice":

        instructions = f"""
Generate EXACTLY {number} multiple-choice questions.

Requirements:
- Four options labelled A, B, C and D.
- Only ONE correct answer.
- State the correct answer.
- Briefly explain why the answer is correct.
"""

    elif question_type == "short answer":

        instructions = f"""
Generate EXACTLY {number} short-answer questions.

Requirements:
- Provide a concise answer after each question.
- Keep answers under three sentences.
"""

    elif question_type in ["true/false", "true false", "true / false"]:

        instructions = f"""
Generate EXACTLY {number} True/False questions.

Requirements:
- State whether each statement is True or False.
- Provide a one-sentence explanation.
"""

    elif question_type == "essay":

        instructions = f"""
Generate EXACTLY {number} essay questions.

Requirements:
- Encourage critical thinking.
- Do NOT provide answers.
"""

    else:

        instructions = f"""
Generate EXACTLY {number} study questions.
"""

    prompt = f"""
You are an experienced university lecturer and assessment designer.

Your task is to create high-quality revision questions based ONLY on the study material provided.

Difficulty Level:
{difficulty}

Question Type:
{question_type.title()}

Instructions:
{instructions}

General Rules:

1. Use ONLY information from the study material.
2. Do NOT invent facts or add outside knowledge.
3. Cover different concepts where possible.
4. Avoid duplicate or very similar questions.
5. Write clear, grammatically correct English.
6. Number every question.
7. Follow the requested format exactly.

Study Material
========================

{text}

========================

Now generate the questions.
"""

    return prompt