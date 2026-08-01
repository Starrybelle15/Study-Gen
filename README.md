# Auto QGen AI

QGen-AI is an AI-powered educational assistant that automatically generates study and review questions from lecture notes, files.
<img width="2000" height="2000" alt="4" src="https://github.com/user-attachments/assets/c2041216-2c37-42e4-8fd1-9439907f67a1" />


## Features

You have choices ranging from:
- Upload PDF
- Upload DOCX
- Upload TXT
- Paste Notes

And you can also decide how you want the questions, like:
- Multiple Choice Questions
- Short Answer Questions
- Essay Questions
- True/False Questions
- Difficulty Levels

Plus and option to
- Download Questions as DOCX

## Technologies
I used a couple of libraries, dependencies and pretrained models for this, some of the main ones include:
- Python
- Gradio
- Hugging Face Inference API
- QWen Model
- pdfplumber
- python-docx

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env`

```env
HF_TOKEN=YOUR_TOKEN
MODEL_NAME=Qwen/Qwen2.5-7B-Instruct
```

Run

```bash
python app.py
```

---
I chose using an Inference API over Transformers, because pulling the models into my codespaces became a hassle, and also I did not have the computing power to load a 7b model locally

Developed as an AI-powered educational tool to aid students preparing for exams or just revising notes.
