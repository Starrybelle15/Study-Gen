import tempfile
from pathlib import Path

import gradio as gr

from exporter import export_docx

from generator import generate_questions
from readers import read_file


# --------------------------------------------------
# Main Processing Function
# --------------------------------------------------

def process_document(
    uploaded_file,
    pasted_notes,
    question_type,
    difficulty,
    number,
):

    try:

        # Get text
        if uploaded_file is not None:

            text = read_file(uploaded_file)

        elif pasted_notes.strip():

            text = pasted_notes

        else:

            return (
                "Please upload a document or paste some study notes.",
                None,
            )

        # Generate questions
        questions = generate_questions(
            text=text,
            question_type=question_type,
            difficulty=difficulty,
            number=int(number),
        )

        # Export DOCX
        docx_file = export_docx(questions)

        return questions, docx_file

    except Exception as e:

        return f"Error:\n\n{e}", None


# --------------------------------------------------
# Interface
# --------------------------------------------------

theme = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="indigo",
)

with gr.Blocks(
    title="StudyGen AI",
    theme=theme,
) as demo:

    gr.Image(
    "assets/banner.png",
    show_label=False,
    show_download_button=True,
    height=220,
)

    gr.Markdown(
        """
# 📚 StudyGen AI

Generate study questions in seconds, from:

- PDF
- DOCX
- TXT
- Pasted Notes

Powered by Hugging Face AI.
"""
    )

    with gr.Row():

        with gr.Column():

            upload = gr.File(
                label="Upload Study Material",
                file_types=[
                    ".pdf",
                    ".docx",
                    ".txt",
                ],
            )

            notes = gr.Textbox(
                label="Or Paste Notes",
                lines=12,
                placeholder="Paste your lecture notes here...",
            )

            question_type = gr.Dropdown(
                choices=[
                    "Multiple Choice",
                    "Short Answer",
                    "True/False",
                    "Essay",
                ],
                value="Multiple Choice",
                label="Question Type",
            )

            difficulty = gr.Dropdown(
                choices=[
                    "Easy",
                    "Medium",
                    "Hard",
                ],
                value="Medium",
                label="Difficulty",
            )

            number = gr.Slider(
                minimum=1,
                maximum=20,
                value=5,
                step=1,
                label="Number of Questions",
            )

            generate_button = gr.Button(
                "🚀 Generate Questions",
                variant="primary",
            )

        with gr.Column():

            output = gr.Textbox(
                label="Generated Questions",
                lines=24,
                show_copy_button=True,
            )

            download = gr.File(
                label="Download DOCX",
            )

    gr.Examples(
        examples=[
            [
                None,
                """Artificial Intelligence enables computers to perform tasks that normally require human intelligence.

Machine Learning is a subset of Artificial Intelligence.

Deep Learning is a subset of Machine Learning.

Supervised Learning uses labelled data.

Unsupervised Learning identifies hidden patterns.

Reinforcement Learning learns using rewards and penalties.""",
                "Multiple Choice",
                "Medium",
                5,
            ]
        ],
        inputs=[
            upload,
            notes,
            question_type,
            difficulty,
            number,
        ],
    )

    generate_button.click(
        fn=process_document,
        inputs=[
            upload,
            notes,
            question_type,
            difficulty,
            number,
        ],
        outputs=[
            output,
            download,
        ],
        show_progress="full",
    )
    show_progress="full"

    gr.Markdown(
        """
---

### StudyGen AI

Built using:

- Python
- Gradio
- Hugging Face Inference API
- pdfplumber
- python-docx

© 2026 StudyGen AI
"""
    )

# --------------------------------------------------
# Launch
# --------------------------------------------------

if __name__ == "__main__":

    demo.launch()