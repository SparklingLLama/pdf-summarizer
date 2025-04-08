import streamlit as st
import fitz  # PyMuPDF
import requests
import os
from dotenv import load_dotenv

# --- LOAD ENV ---
load_dotenv()
TOGETHER_API_KEY=os.getenv("TOGETHER_API_KEY")

# --- DEFINE FUNCTIONS FIRST ---
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def summarize_text_with_together(text):
    prompt = f"""
    Summarize the following PDF content in a structured format:

    - List 5 main bullet points of the content.
    - Add a TLDR in one line at the end.
    - Keep it simple and beginner-friendly.

    Content:
    {text}
    """

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.2",
        "prompt": prompt,
        "max_tokens": 512,
        "temperature": 0.4,
        "top_p": 0.9,
    }

    response = requests.post("https://api.together.xyz/v1/completions", headers=headers, json=payload)
    return response.json()["choices"][0]["text"].strip()

# def summarize_text_with_gpt(text):
    # return "✅ This is a mock summary. Everything is working. Add your API key or change model provider to get real summaries."


# --- STREAMLIT UI ---
st.set_page_config(page_title="AI PDF Summarizer", layout="centered")
st.title("📄 AI PDF Summarizer")
st.write("Upload a PDF and get a smart summary using AI!")

uploaded_file = st.file_uploader("📤 Upload your PDF", type="pdf")

if uploaded_file is not None:
    with st.spinner("📖 Reading your PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)

    with st.spinner("🧠 Summarizing with GPT..."):
        summary = summarize_text_with_together(pdf_text)

    st.subheader("📝 Summary")
    st.write(summary)

    st.download_button(
        label="📥 Download Summary",
        data=summary,
        file_name="summary.txt",
        mime="text/plain"
    )
