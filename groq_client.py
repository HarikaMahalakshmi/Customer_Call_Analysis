import requests
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def analyze_transcript(transcript):
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that summarizes customer calls and detects sentiment."},
            {"role": "user", "content": f"Transcript: {transcript}\n\nProvide:\n1. Short summary (2-3 sentences, no stars).\n2. Sentiment (Positive, Negative, or Neutral).\nAlso give a one-line explanation of why you chose that sentiment."}
        ],
        "temperature": 0.2
    }

    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}

    try:
        response = requests.post(GROQ_API_URL, json=payload, headers=headers, timeout=20)
        response.raise_for_status()
        result = response.json()
        content = result["choices"][0]["message"]["content"]

        # Parse
        summary, sentiment, explanation = "N/A", "N/A", ""
        if "Sentiment:" in content:
            parts = content.split("Sentiment:")
            summary = parts[0].replace("Summary:", "").strip()
            rest = parts[1].strip()
            if "Explanation:" in rest:
                sentiment, explanation = rest.split("Explanation:", 1)
                sentiment = sentiment.strip().capitalize()
                explanation = explanation.strip()
            else:
                sentiment = rest.strip().capitalize()

        return summary, sentiment, explanation
    except Exception as e:
        print(f"[ERROR] Groq API failed: {e}")
        return "Summary unavailable", "Sentiment unavailable", ""
