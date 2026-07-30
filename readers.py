"""
StudyGen AI
readers.py
"""

import pdfplumber
from docx import Document


def read_pdf(path):

    text = ""

    with pdfplumber.open(path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def read_docx(path):

    doc = Document(path)

    return "\n".join(
        paragraph.text
        for paragraph in doc.paragraphs
    )


def read_txt(path):

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def read_file(file):

    if hasattr(file, "name"):
        path = file.name
    else:
        path = str(file)

    path = path.lower()

    if path.endswith(".pdf"):
        return read_pdf(path)

    if path.endswith(".docx"):
        return read_docx(path)

    if path.endswith(".txt"):
        return read_txt(path)

    raise ValueError("Unsupported file type.")