import requests
from bs4 import BeautifulSoup
import time
import os

# ===== 設定 =====
LINE_CHANNEL_TOKEN = os.getenv("LINE_CHANNEL_TOKEN")
LINE_USER_ID = os.getenv("LINE_USER_ID")

def send_line_message(message):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_CHANNEL_TOKEN}"
    }
    data = {
        "to": LINE_USER_ID,
        "messages": [
            {"type": "text", "text": message}
        ]
    }
    requests.post(url, headers=headers, json=data)

# ===== メイン =====
def main():
    print("テスト開始")
    send_line_message("予約に空きが出たで。急いで確認すべし！")
    print("テスト終了")
    return

if __name__ == "__main__":
    main()
