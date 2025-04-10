from flask import Flask, request
import requests
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Chaves de API
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

# Config Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/", methods=["GET"])
def home():
    return "Bot do Telegram com Gemini está no ar!"

@app.route(f"/{TELEGRAM_TOKEN}", methods=["POST"])
def telegram_webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        user_message = data["message"].get("text", "")

        # Gerar resposta com Gemini
        try:
            response = model.generate_content(user_message)
            reply = response.text
        except Exception as e:
            reply = f"Erro com Gemini: {e}"

        # Enviar resposta de volta ao Telegram
        requests.post(f"{TELEGRAM_URL}/sendMessage", json={
            "chat_id": chat_id,
            "text": reply,
        })

    return "ok", 200
