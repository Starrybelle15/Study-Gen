# StudyGen AI

StudyGen AI is an AI-powered educational assistant that automatically generates study questions from lecture notes.

## Features

- Upload PDF
- Upload DOCX
- Upload TXT
- Paste Notes
- Multiple Choice Questions
- Short Answer Questions
- Essay Questions
- True/False Questions
- Difficulty Levels
- Download Questions as DOCX

## Technologies

- Python
- Gradio
- Hugging Face Inference API
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

Developed as an AI-powered educational tool.