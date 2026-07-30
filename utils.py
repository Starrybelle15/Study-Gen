"""
StudyGen AI
Utility Functions
"""


def clean_text(text):
    """
    Clean extracted document text.
    """

    if not text:
        return ""

    text = text.replace("\r", " ")
    text = text.replace("\n", " ")

    while "  " in text:
        text = text.replace("  ", " ")

    return text.strip()


def split_into_chunks(text, max_words=250):
    """
    Split long documents into manageable chunks.
    """

    words = text.split()

    chunks = []

    for i in range(0, len(words), max_words):

        chunk = words[i:i + max_words]

        chunks.append(" ".join(chunk))

    return chunks