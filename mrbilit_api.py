import requests
import json


def mrbilit_sms(phone: str):
    phone = "0" + phone
    resp_sms = requests.get(
        f"https://auth.mrbilit.com/api/login/exists/v2?mobileOrEmail={phone}&source=2&sendTokenIfNot=true",
        headers={"Content-Type": "application/json",
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    try:
        status_sms = resp_sms.json()
        print("Mrbilit_Done")
        return True
    except Exception as e:
        print(f"Mrbilit_Failed, {e}")
        return False
