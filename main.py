from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    msg = data.get("message", "No message content")
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"📢 TradingView Alert:\n{msg}"
    }
    requests.post(url, json=payload)
    return 'Alert sent!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
