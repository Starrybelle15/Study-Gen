"""
StudyGen AI
prompts.py

Builds prompts for the AI model.
"""


def build_prompt(text, question_type, difficulty, number):
    """
    Build a structured prompt for question generation.
    """

    return f"""
You are an expert university lecturer, examiner, and instructional designer.

Your job is to generate high-quality study questions using ONLY the study material provided.

=========================
RULES
=========================

1. Use ONLY the supplied notes.
2. Do NOT invent facts.
3. Do NOT use outside knowledge.
4. Do NOT include answers.
5. Produce EXACTLY {number} questions.
6. Number each question.
7. Match the requested difficulty.
8. Make the wording clear and professional.
9. Avoid duplicate questions.
10. Ensure every question is relevant to the notes.

=========================
QUESTION SETTINGS
=========================

Question Type:
{question_type}

Difficulty:
{difficulty}

=========================
STUDY NOTES
=========================

{text}

=========================
OUTPUT FORMAT
=========================

1. Question one

2. Question two

3. Question three

Continue until exactly {number} questions have been produced.

Do not include explanations.

Do not include answers.

Only return the questions.
"""