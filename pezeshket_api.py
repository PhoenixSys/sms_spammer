import requests
import json


def pezeshket_sms(phone: str):
    resp_sms = requests.post("https://api.pezeshket.com/core/v1/auth/requestCode",
                             data=json.dumps(
                                 {"mobileNumber": phone}),
                             headers={"Content-Type": "application/json",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    try:
        status_sms = resp_sms.json()["codeLength"]
        if status_sms == 5:
            print("Pezeshket_Done")
            return True
        else:
            print("Pezeshket_Failed")
            return False
    except Exception as e:
        print(f"Pezeshket_Failed, {e}")
        return False
