"""
StudyGen AI
Prompt templates for question generation.
"""


def build_prompt(text, question_type, difficulty, number):
    """
    Create a prompt for the FLAN-T5 model.
    """

    question_type = question_type.strip().lower()

    if question_type == "short answer":

        instruction = f"""
Generate exactly {number} short-answer questions.

Requirements:
- Number each question.
- Provide a short answer after each question.
- Cover different concepts from the material.
"""

    elif question_type == "multiple choice":

        instruction = f"""
Generate exactly {number} multiple-choice questions.

Requirements:
- Four options (A, B, C, D)
- One correct answer
- Show the correct answer after each question.
"""

    elif question_type == "true / false":

        instruction = f"""
Generate exactly {number} True/False questions.

Requirements:
- State True or False.
- Provide the correct answer after each question.
"""

    elif question_type == "essay":

        instruction = f"""
Generate exactly {number} essay questions.

Requirements:
- Encourage critical thinking.
- Questions should require detailed explanations.
"""

    else:

        instruction = f"""
Generate exactly {number} study questions.
"""

    prompt = f"""
You are an experienced university lecturer.

Create revision questions from the study material below.

Difficulty: {difficulty}

{instruction}

Study Material
--------------
{text}
"""

    return prompt

