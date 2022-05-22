import requests
import json


def banikar_sms(phone: str):
    phone = "0" + phone
    resp_sms = requests.post("https://api.banikar.com/api/v1/auth/send/",
                             data=json.dumps(
                                 {"mobile_number": phone}),
                             headers={"Content-Type": "application/json",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    try:
        status_sms = resp_sms.json()['meta']['code']
        if status_sms == 200:
            print("Banikar_Done")
            return True
        else:
            print("Banikar_Failed")
            return False
    except Exception as e:
        print(f"Banikar_Failed, {e}")
        return False
