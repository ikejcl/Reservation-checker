import requests
from bs4 import BeautifulSoup
import time
import os

# ===== 設定 =====
URL = os.getenv("TARGET_URL")  # Railway の環境変数で設定する
LINE_TOKEN = os.getenv("LINE_TOKEN")  # LINE Notify のトークンも環境変数で設定

CHECK_INTERVAL = 300  # 5分ごとにチェック（秒）

# ===== LINE通知 =====
def send_line_notify(message):
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {LINE_TOKEN}"}
    data = {"message": message}
    try:
        requests.post(url, headers=headers, data=data)
    except Exception as e:
        print("LINE通知エラー:", e)

# ===== 空き枠チェック =====
def check_reservation():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print("ページ取得エラー:", e)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # ★ 予約サイトに合わせてここを書き換える ★
    # 例：ページ内に「空きあり」という文字があれば通知
    if "空き" in soup.text or "予約可能" in soup.text:
        send_line_notify("予約に空きが出ました！急いで確認してください！")

# ===== メインループ =====
def main():
    print("予約監視を開始します…")
    while True:
        check_reservation()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
