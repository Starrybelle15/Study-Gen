from generator import generate_questions

notes = """
Artificial Intelligence (AI) enables machines to perform tasks
that normally require human intelligence.

Machine Learning is a subset of AI.

Deep Learning is a subset of Machine Learning.

Supervised learning uses labelled data.

Unsupervised learning discovers hidden patterns.

Reinforcement learning learns through rewards and penalties.
"""

questions = generate_questions(
    text=notes,
    question_type="Multiple Choice",
    difficulty="Medium",
    number=5
)

print("\n")
print("=" * 60)
print("GENERATED QUESTIONS")
print("=" * 60)
print(questions)