import streamlit as st
import ollama
from PyPDF2 import PdfReader
from docx import Document


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Notes Summarizer",
    page_icon="📝"
)

st.title("📝 AI Notes Summarizer")
st.write("Upload your notes and get an AI-generated summary.")


# -----------------------------
# Read PDF
# -----------------------------
def read_pdf(file):
    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# -----------------------------
# Read DOCX
# -----------------------------
def read_docx(file):
    document = Document(file)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


# -----------------------------
# Read TXT
# -----------------------------
def read_txt(file):
    return file.read().decode("utf-8")


# -----------------------------
# Upload File
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload your notes",
    type=["pdf", "docx", "txt"]
)


# -----------------------------
# Process Uploaded File
# -----------------------------
if uploaded_file:

    st.success("File uploaded successfully!")

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        notes = read_pdf(uploaded_file)

    elif file_name.endswith(".docx"):
        notes = read_docx(uploaded_file)

    elif file_name.endswith(".txt"):
        notes = read_txt(uploaded_file)

    else:
        st.error("Unsupported file type.")
        st.stop()


    # -----------------------------
    # Check if notes are empty
    # -----------------------------
    if not notes.strip():
        st.warning("No text could be extracted from this file.")
        st.stop()


    # -----------------------------
    # Show Notes
    # -----------------------------
    with st.expander("📖 View Your Notes"):
        st.text(notes)


    # -----------------------------
    # Summarize Notes
    # -----------------------------
    if st.button("✨ Summarize Notes"):

        with st.spinner("🤖 AI is summarizing..."):

            prompt = f"""
You are an AI notes summarizer.

Summarize the following notes using simple and easy-to-understand language.

Use exactly this format:

## SUMMARY
Write a short summary of the notes.

## IMPORTANT POINTS
- Point 1
- Point 2
- Point 3

## KEY TAKEAWAYS
- Takeaway 1
- Takeaway 2
- Takeaway 3

NOTES:
{notes}
"""

            try:
                response = ollama.chat(
                    model="llama3",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                summary = response["message"]["content"]

                st.subheader("📄 AI Summary")
                st.markdown(summary)

            except Exception as e:
                st.error(
                    f"Error while communicating with Ollama: {e}"
                )


