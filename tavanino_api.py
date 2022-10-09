import requests, json


def tavanino_sms(phone: str):
    phone = "0" + phone
    resp_sms = requests.post("https://tavanino.com/login/?sendOTPCode=1",
                             data=f'username={phone}&isRegister=1',
                             headers={"Content-Type": "application/x-www-form-urlencoded"})
    try:
        status_sms = resp_sms.json()
        if status_sms["status"] == 1:
            print("Tavanino_Done")
            return True
        else:
            print("Tavanino_Failed")
            return False
    except Exception as e:
        print("Tavanino_Failed")
        return False
