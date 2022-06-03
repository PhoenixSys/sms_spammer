import requests
import json


def tikban_sms(phone: str):
    phone1 = "0" + phone
    resp_sms = requests.post("https://tikban.com/Account/SendTokenForLogin",
                             data=json.dumps(
                                 {"JustMobilephone": phone, "username": phone1, "phoneNumberCode": "+98",
                                  "CaptchaKey": None}),
                             headers={"Content-Type": "application/json",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    try:
        status_sms = resp_sms.json()["HasError"]
        if status_sms is False:
            print("Tikban_Done")
            return True
        else:
            print("Tikban_Failed")
            return False
    except Exception as e:
        print(f"Tikban_Failed, {e}")
        return False
