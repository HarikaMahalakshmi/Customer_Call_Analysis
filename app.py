from flask import Flask, render_template, request
import csv
import os
from groq_client import analyze_transcript

app = Flask(__name__)
CSV_FILE = "call_analysis.csv"

@app.route("/", methods=["GET", "POST"])
def index():
    summary, sentiment, explanation, transcript = "", "", "", ""
    if request.method == "POST":
        transcript = request.form["transcript"]
        summary, sentiment, explanation = analyze_transcript(transcript)

        # Save clean data into CSV
        save_to_csv(transcript, summary, sentiment)

    return render_template(
        "index.html",
        transcript=transcript,
        summary=summary,
        sentiment=sentiment,
        explanation=explanation
    )

def save_to_csv(transcript, summary, sentiment):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Transcript", "Summary", "Sentiment"])
        writer.writerow([transcript, summary, sentiment])

if __name__ == "__main__":
    app.run(debug=True)
