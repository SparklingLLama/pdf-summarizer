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
    api_key = os.getenv("TOGETHER_API_KEY")

    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",  # or your chosen model
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that summarizes PDFs."},
            {"role": "user", "content": f"Summarize this:\n\n{text}"}
        ],
        "max_tokens": 500,
        "temperature": 0.4
    }

    response = requests.post(url, headers=headers, json=payload)
    result = response.json()


    # Handle errors gracefully
    if "choices" in result and len(result["choices"]) > 0:
        return result["choices"][0]["message"]["content"].strip()
    else:
        return "Sorry, I couldn't generate a summary. Please try again later."

# --- STREAMLIT UI ---
st.set_page_config(page_title="AI PDF Summarizer", layout="centered")
st.title("📄 AI PDF Summarizer")
st.write("Upload a PDF and get a smart summary using AI!")

uploaded_file = st.file_uploader("📤 Upload your PDF", type="pdf")

if uploaded_file is not None:
    with st.spinner("📖 Reading your PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)

    with st.spinner("🧠 Summarizing with AI..."):
        summary = summarize_text_with_together(pdf_text)

    st.subheader("📝 Summary")
    st.write(summary)

    st.download_button(
        label="📥 Download Summary",
        data=summary,
        file_name="summary.txt",
        mime="text/plain"
    )

