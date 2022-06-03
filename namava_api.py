import requests
import json


def namava_api(phone: str):
    phone = "+98" + phone
    resp_sms = requests.post("https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",
                             data=json.dumps(
                                 {"UserName": phone}),
                             headers={"Content-Type": "application/json",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    try:
        status_sms = resp_sms.json()["succeeded"]
        if status_sms:
            print("Namava_Done")
            return True
        else:
            print("Namava_Failed")
            return False
    except Exception as e:
        print(f"Namava_Failed, {e}")
        return False
