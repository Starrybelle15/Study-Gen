from codespace.prompt import build_prompt

prompt = build_prompt(
    text="Machine Learning is a branch of Artificial Intelligence that enables computers to learn from data.",
    question_type="Short Answer",
    difficulty="Easy",
    number=3
)

print(prompt)