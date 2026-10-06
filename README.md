# AI-NOTES-SUMMARIZER

## 📌 Project Description

**AI Notes Summarizer** is a Python-based application that uses Artificial Intelligence to automatically summarize study notes and documents.

The application provides a simple **Streamlit web interface** where users can upload their notes or PDF documents. The content is extracted and sent to an AI model through **Ollama**, which generates a concise and easy-to-understand summary.

This project helps students save time by converting lengthy study materials into short and useful summaries.

---

## ✨ Features

* 📄 Upload PDF notes
* 🤖 AI-powered text summarization
* 📝 Generate concise summaries
* 🎓 Useful for students and study materials
* 🌐 Simple and interactive Streamlit interface
* 🔒 Can run locally using Ollama
* ⚡ Fast document processing
* 📥 Easy-to-use interface

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit** – Web application interface
* **Ollama** – Local AI model
* **PyPDF2** – PDF text extraction
* **python-docx** – Word document processing

---

## 📂 Project Structure

```text
AI-Notes-Summarizer/
│
├── app.py
├── README.md
├── requirements.txt
│
└── sample_notes/
    └── notes.pdf
```

---

## ⚙️ Installation

### 1. Install Python

Make sure Python is installed on your computer.

Check the installation:

```bash
python --version
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Required Libraries

```bash
pip install streamlit ollama PyPDF2 python-docx
```

You can also create a `requirements.txt` file:

```text
streamlit
ollama
PyPDF2
python-docx
```

Then install everything using:

```bash
pip install -r requirements.txt
```

---

## 🤖 Ollama Setup

Install Ollama on your computer and download an AI model.

For example:

```bash
ollama pull llama3.2
```

Check the available models:

```bash
ollama list
```

Make sure the Ollama service is running before starting the application.

---

## ▶️ How to Run the Project

Open the project folder in Command Prompt or PowerShell.

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Run the Streamlit application:

```bash
streamlit run app.py
```

Streamlit will start the application in your web browser.

---

## 📖 How the Application Works

The application follows these steps:

```text
User
  ↓
Upload Notes / PDF
  ↓
Extract Text
  ↓
Send Text to AI Model
  ↓
Ollama Generates Summary
  ↓
Display Summary
```

### Step 1: Upload Notes

The user uploads a PDF or supported document through the Streamlit interface.

### Step 2: Extract Text

The application reads the uploaded document and extracts its text.

### Step 3: AI Processing

The extracted text is sent to the Ollama AI model.

### Step 4: Generate Summary

The AI analyzes the notes and produces a shorter summary containing the important information.

### Step 5: Display Result

The generated summary is displayed on the Streamlit web page.

---

## 💻 Example

### Input

```text
Artificial Intelligence is a branch of computer science
that enables machines to perform tasks that normally require
human intelligence. AI applications include learning,
reasoning, problem solving and decision making.
```

### Output

```text
Summary:

Artificial Intelligence enables computers to perform
human-like tasks such as learning, reasoning,
problem solving and decision making.
```

---

## 🎯 Objectives

* To develop an AI-based notes summarization system.
* To reduce the time required to read lengthy documents.
* To provide students with concise study material.
* To demonstrate the use of AI with Python.
* To create an easy-to-use web application.

---

## 🌟 Advantages

* Saves study time.
* Reduces lengthy content.
* Easy to use.
* Works locally with Ollama.
* Helpful for revision and exam preparation.
* Provides quick access to important information.

---

## 🔮 Future Enhancements

The project can be improved by adding:

* 📑 Multiple PDF upload
* 📊 Key-point extraction
* ❓ Automatic question generation
* 🧠 Quiz generation
* 🔊 Text-to-speech summaries
* 🌍 Multiple-language summaries
* 📥 Download summary as PDF or DOCX
* 💬 Chat with uploaded notes

---

## ⚠️ Limitations

* Summary quality depends on the AI model.
* Very large documents may require additional processing.
* Scanned PDFs may require OCR for text extraction.
* Ollama and the selected AI model must be installed locally.

---

## 📜 License

This project is developed for **educational and academic purposes**.

---

## 👨‍💻 Author

**AI Notes Summarizer Project**

Developed using **Python, Streamlit, and Ollama**.

---

## 📚 References

* Streamlit Documentation
* Python Documentation
* Ollama Documentation
* PyPDF2 Documentation
* python-docx Documentation
