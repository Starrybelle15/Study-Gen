"""
StudyGen AI
Document Readers
"""

import os
import pdfplumber
from docx import Document


def read_pdf(path):
    """
    Extract text from a PDF file.
    """
    text = ""

    with pdfplumber.open(path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def read_docx(path):
    """
    Extract text from a DOCX file.
    """
    doc = Document(path)

    text = "\n".join(
        paragraph.text
        for paragraph in doc.paragraphs
    )

    return text


def read_txt(path):
    """
    Extract text from a TXT file.
    """
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def extract_text(file_path):
    """
    Detect the file type and extract text.
    """

    if not file_path:
        return ""

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return read_pdf(file_path)

    elif extension == ".docx":
        return read_docx(file_path)

    elif extension == ".txt":
        return read_txt(file_path)

    else:
        raise ValueError(
            f"Unsupported file format: {extension}"
        )