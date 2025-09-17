# 📞 Customer Call Analysis – Flask + Groq API  

## 🔹 Project Overview  
This is a **Flask web application** that analyzes customer call transcripts using the **Groq Llama 3.1 model**.  

The app:  
- 📝 Summarizes the transcript in **2–3 sentences**  
- 😊 Detects the **sentiment** (Positive / Negative / Neutral)  
- 💬 Explains why that sentiment was chosen  
- 💾 Saves all analyses in a **CSV file** (`Transcript | Summary | Sentiment`)  

---

## 🔹 Features  
✅ Clean **web UI** with Bootstrap styling + Dark/Light mode toggle  
✅ **Summarization + sentiment detection** in real time  
✅ Results shown with **emoji + color-coded badges**  
✅ One-click **explanation reveal**  
✅ All outputs saved in **`call_analysis.csv`**  

---

## 🔹 Tech Stack  
- **Backend**: Python (Flask)  
- **Frontend**: HTML, CSS, Bootstrap, Jinja2  
- **AI Model**: Groq `llama-3.1-8b-instant`  
- **Storage**: CSV logging  
- **Deployment**: Render (Gunicorn)  

---

## 🔹 Setup & Run Locally  

### 1. Clone repo  
### 2. Create virtual environment
### 3. Install dependencies

``` pip install -r requirements.txt```

### 4. Set API Key

Create a file named .env in the project root and add:

GROQ_API_KEY=your_api_key_here

### 5. Run the app

``` python app.py ```

Now open in your browser → http://127.0.0.1:5000/

