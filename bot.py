import json
import requests

TOKEN = "TU_BOT_TOKEN"
API = f"https://api.telegram.org/bot{TOKEN}"

def send(chat_id, msg):
    requests.post(
        f"{API}/sendMessage",
        data={"chat_id": chat_id, "text": msg}
    )

def load():
    with open("data.json") as f:
        return json.load(f)

def save(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)

def handle(chat_id, text):
    data = load()

    if text.startswith("/add"):
        try:
            _, keyword, price = text.split()
            data["searches"].append({
                "keyword": keyword,
                "price": int(price),
                "last_id": None
            })
            save(data)
            send(chat_id, "✅ Búsqueda añadida")
        except:
            send(chat_id, "❌ Uso: /add palabra precio")

    elif text == "/list":
        msg = "📋 Búsquedas:\n"
        for i, s in enumerate(data["searches"]):
            msg += f"{i+1}. {s['keyword']} ≤ {s['price']}€\n"
        send(chat_id, msg)
