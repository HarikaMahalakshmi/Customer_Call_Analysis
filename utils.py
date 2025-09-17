import pandas as pd
import os

CSV_FILE = "call_analysis.csv"

def save_to_csv(transcript, summary, sentiment):
    """
    Save the call analysis result to CSV
    """
    file_exists = os.path.isfile(CSV_FILE)
    df = pd.DataFrame([{
        "Transcript": transcript,
        "Summary": summary,
        "Sentiment": sentiment
    }])
    if file_exists:
        df.to_csv(CSV_FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(CSV_FILE, index=False)
