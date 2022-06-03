import requests
import json


def virgol_sms(phone: str):
    phone = "+98" + phone
    resp_sms = requests.post("https://virgool.io/api/v1.4/auth/verify",
                             data=json.dumps(
                                 {"method": "phone", "identifier": phone}),
                             headers={"Content-Type": "application/json",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    try:
        status_sms = resp_sms.json()["success"]
        if status_sms:
            print("Virgol_Done")
            return True
        else:
            print("Virgol_Failed")
            return False
    except Exception as e:
        print(f"Virgol_Failed, {e}")
        return False
