import os
import nltk
from flask import Flask, request, jsonify
from textblob_de import TextBlobDE
# Initialisiere die Flask-Anwendung
app = Flask(__name__)

# NLP-Datenpfad setzen
nltk.data.path.append(os.path.join(os.path.dirname(__file__), "nltk_data"))
@app.route('/analyze', methods=['POST'])
def analyze_text():
 data = request.get_json()
 text = data.get("text", "")
 if not text:
 return jsonify({"error": "Kein Text erhalten"}), 400
 # Sentiment-Analyse mit TextBlob
 sentiment_score = TextBlobDE(text).sentiment.polarity
 if sentiment_score > 0:
 sentiment = "Positiv"
 elif sentiment_score < 0:
 sentiment = "Negativ"
 else:
 sentiment = "Neutral"
Seite 5 von 9
 return jsonify({"sentiment": sentiment, "score": sentiment_score})
# Sicherstellen, dass die NLP-Daten richtig geladen werden
NLTK_PATH = os.path.join(os.path.dirname(__file__), "nltk_data")
nltk.data.path.append(NLTK_PATH)
@app.route('/debug_nlp', methods=['GET'])
def debug_nlp():
 test_text = "Ich liebe dieses Produkt!"
 blob = TextBlobDE(test_text)
 sentiment_score = blob.sentiment.polarity
 # Debugging-Ausgaben
 return {
 "Text": test_text,
 "Polarity": sentiment_score,
 "NLTK Path": nltk.data.path,
 "NLTK Data Exists": os.path.exists(NLTK_PATH)
 }
# Hauptprogramm: Flask-Server starten
if __name__ == "__main__":
 # Stelle sicher, dass die App auf Port 8000 läuft
 app.run(host="0.0.0.0", port=8000) 