import requests
import json


def tamland_api(phone: str):
    phone = "0" + phone
    resp_sms = requests.post("https://api.tamland.ir/api/user/signup",
                             data=json.dumps(
                                 {"Mobile": phone, "SchoolId": -1}),
                             headers={"Content-Type": "application/json",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    try:
        status_sms = resp_sms.json()
        print("Tamland_Done")
        return True
    except Exception as e:
        print(f"Tamland_Failed, {e}")
        return False
