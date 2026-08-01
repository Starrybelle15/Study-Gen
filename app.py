import gradio as gr

from exporter import export_docx
from generator import generate_questions
from readers import read_file

from pathlib import Path

#css = """
#body {
 #   background: url("/gradio_api/file=assets/bg.webp") no-repeat center center fixed;
  #  background-size: cover;
#}

#.gradio-container {
 #   background: transparent !important;
#}
#"""

css = """
/* ===============================
   Background
================================ */

body{
    background:url("/gradio_api/file=assets/bg.webp");
    background-size:cover;
    background-position:center;
    background-repeat:no-repeat;
    background-attachment:fixed;
}

.gradio-container{
    background:rgba(8,15,30,.55)!important;
    backdrop-filter:blur(8px);
}


/* ===============================
   Header
================================ */

h1{
    color:white !important;
    font-size:42px !important;
    font-weight:700;
}

h2,h3,h4{
    color:#dbeafe !important;
}

p{
    color:#e5e7eb !important;
}


/* ===============================
   Cards
================================ */

.gr-group,
.gr-box,
.block{
    background:rgba(255,255,255,.12)!important;
    backdrop-filter:blur(16px);
    border-radius:20px !important;
    border:1px solid rgba(255,255,255,.15)!important;
}


/* ===============================
   Upload Box
================================ */

.gr-file{
    border:2px dashed #60a5fa !important;
    border-radius:18px !important;
}


/* ===============================
   Textboxes
================================ */

textarea{
    background:rgba(255,255,255,.95)!important;
    border-radius:14px!important;
}

input{
    background:white!important;
}


/* ===============================
   Dropdowns
================================ */

select{
    border-radius:12px!important;
}


/* ===============================
   Slider
================================ */

input[type=range]{
    accent-color:#2563eb;
}


/* ===============================
   Button
================================ */

button{
    background:linear-gradient(135deg,#2563eb,#7c3aed)!important;
    color:white!important;
    border:none!important;
    border-radius:14px!important;
    font-size:18px!important;
    font-weight:600!important;
    transition:.3s;
}

button:hover{
    transform:translateY(-2px);
    box-shadow:0 10px 25px rgba(37,99,235,.4);
}


/* ===============================
   Footer
================================ */

hr{
    border-color:rgba(255,255,255,.2);
}
"""
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
    css=css,
    title="StudyGen AI"
) as demo:
 
    # Banner
   # gr.HTML("""
    #<div style="text-align:center;">
     #   <img src="/gradio_api/file=assets/a qgen ai.png"
      #       style="width:100%;
       #             max-width:1200px;
        #            border-radius:12px;">
    #</div>
    #""")
    # BANNER = Path("assets/a qgen ai.png")

  #  gr.HTML("""
#<div style="text-align:center; margin-bottom:20px;">
 #   <img src="/gradio_api/file=assets/callum.png"
         #style="width:280px; height:auto;">
#</div>
#""")

    # Logo + Title
    with gr.Row():
        # Banner image
        gr.Image(
            value="assets/callum.png",
            label=None,
            height=120,
            width=180,
            container=False,
            interactive=False
    )

    gr.Markdown("# 📚 Auto QGen-AI")
    gr.Markdown("### AI-Powered Automated Question Generator")

    gr.Markdown(

        """
    "# 🧾 QGen-AI
   Generate study and revision questions in seconds, using from:
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

    gr.Markdown(
        """
---

### Auto QGen-AI

Built using:

- Python
- Gradio 6
- Hugging Face Inference API
- pdfplumber
- python-docx

© 2026 QGen AI
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
        share=True,
    )