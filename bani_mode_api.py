import requests, json


def bani_mode_sms(phone: str):
    phone = "0" + phone
    resp_sms = requests.post("https://mobapi.banimode.com/api/v2/auth/request",
                             data=json.dumps(
                                 {"phone": phone}),
                             headers={"Content-Type": "application/json"})
    try:
        status_sms = resp_sms.json()["status"]
        if status_sms == "success":
            print("Bani_Mode_Done")
            return True
        else:
            print("Bani_Mode_Failed")
            return False
    except Exception as e:
        print("Bani_Mode_Failed")
        return False
