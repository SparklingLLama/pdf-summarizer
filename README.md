# 🧠 AI PDF Summarizer

A simple and smart PDF summarization tool built with Streamlit and Together.ai. Upload any PDF and get an instant AI-generated summary in seconds!

---

## 🚀 Features

- 📄 Upload any PDF file  
- 🤖 Summarize content using Together.ai's LLM  
- 📥 Download the summary as a text file  
- ☁️ Ready for deployment on Streamlit Cloud  
- 🛠️ Coming soon:  
  - Extract questions from PDFs  
  - Chat with your PDF  
  - Voice note summarization  

---

## 📦 Tech Stack

- Python 3.10+  
- Streamlit  
- PyMuPDF (`fitz`)  
- Together.ai API  
- `python-dotenv`  

---

## 🖥️ Local Setup

1. **Clone the repository**

       git clone https://github.com/your-username/pdf-summarizer.git
       cd pdf-summarizer

2. **Install dependencies**

       pip install -r requirements.txt

3. **Add your Together.ai API key**

   Create a `.env` file in the root folder with this line:

       TOGETHER_API_KEY=your_together_api_key_here

4. **Run the app**

       streamlit run app.py

---

## 🌐 Deploy to Streamlit Cloud

1. Push your project to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click “New App” and choose your repo
4. Set `app.py` as the main file
5. Add your API key under "Secrets":

       TOGETHER_API_KEY = "your_together_api_key_here"

6. Click **Deploy**

---

## 📌 Prompt Template Sent to Together.ai

> Summarize the following PDF content in a structured format:  
> - List 5 main bullet points of the content  
> - Add a TLDR in one line at the end  
> - Keep it simple and beginner-friendly  

---

## 🧭 Roadmap

- [ ] Extract questions from PDF  
- [ ] Voice note summarization  
- [ ] Chat with PDF (Q&A)  
- [ ] User login/authentication  
- [ ] Stripe/paywall integration  

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome!  
Feel free to fork this repo and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## ✨ Credits

Built with 💙 by [Your Name](https://github.com/your-username)
