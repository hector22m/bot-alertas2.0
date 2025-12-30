import time
import requests
from bot import handle

TOKEN = "TU_BOT_TOKEN"
API = f"https://api.telegram.org/bot{TOKEN}"

offset = 0

while True:
    r = requests.get(
        f"{API}/getUpdates",
        params={"offset": offset, "timeout": 60}
    ).json()

    for u in r.get("result", []):
        offset = u["update_id"] + 1
        chat_id = u["message"]["chat"]["id"]
        text = u["message"]["text"]
        handle(chat_id, text)

    time.sleep(1)

