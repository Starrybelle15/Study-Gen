import gradio as gr

from exporter import export_docx
from generator import generate_questions
from readers import read_file

from pathlib import Path

BANNER = Path("assets/a qgen ai.png")

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

        # Get text from uploaded file or pasted notes
        if uploaded_file is not None:

            text = read_file(uploaded_file)

        elif pasted_notes and pasted_notes.strip():

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

with gr.Blocks(
    title="StudyGen AI"
) as demo:


    # Banner image
    gr.Image(
    value="assets/callum.png",
    label=None,
    height=220,
)

    gr.Image(
        value=str(BANNER),
        show_label=False,
        show_download_button=False,
        interactive=False,
        container=False,
    )

    gr.Markdown("# 📚 Auto QGen-AI")
    gr.Markdown("### AI-Powered Question Generator")

    gr.Markdown(
        """
# 📚 QGen-AI

Generate study and revision questions in seconds from:

- PDF
- DOCX
- TXT
- Pasted Notes

Powered by Hugging Face AI.
"""
    )


    with gr.Row():


        # -------------------------------
        # Input Column
        # -------------------------------

        with gr.Column():

            upload = gr.File(
                label="Upload Study Material",
                file_types=[
                    ".pdf",
                    ".docx",
                    ".txt",
                ],
                type="filepath",
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



        # -------------------------------
        # Output Column
        # -------------------------------

        with gr.Column():

            output = gr.Textbox(
                label="Generated Questions",
                lines=24,
            )


            download = gr.File(
                label="Download DOCX",
            )



    # -------------------------------
    # Example
    # -------------------------------

    gr.Examples(
        examples=[
            [
                None,
                """
Artificial Intelligence enables computers to perform tasks that normally require human intelligence.

Machine Learning is a subset of Artificial Intelligence.

Deep Learning is a subset of Machine Learning.

Supervised Learning uses labelled data.

Unsupervised Learning identifies hidden patterns.

Reinforcement Learning learns using rewards and penalties.
""",
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



    # -------------------------------
    # Button Action
    # -------------------------------

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
    )

    gr.HTML("""
<div style="text-align:center;">
    <img src="file/assets/banner.png"
         style="width:100%;
                max-width:900px;
                border-radius:12px;">
</div>
""")



    gr.Markdown(
        """
---

### StudyGen AI

Built using:

- Python
- Gradio 6
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

    demo.launch(
        theme=gr.themes.Soft(
            primary_hue="blue",
            secondary_hue="indigo",
        ),
        share=False,
    )