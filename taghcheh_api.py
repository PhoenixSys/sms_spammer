import requests, json


def taghcheh_sms(phone: str):
    phone = "0" + phone
    resp_sms = requests.post("https://gw.taaghche.com/v4/site/auth/login",
                             data=json.dumps(
                                 {"contact": phone, "forceOtp": False}),
                             headers={"Content-Type": "application/json"})
    try:
        status_sms = resp_sms.json()["status"]
        if status_sms == 0:
            print("Taghcheh_Done")
            return True
        else:
            print("Taghcheh_Failed")
            return False
    except Exception as e:
        print("Taghcheh_Failed")
        return False
