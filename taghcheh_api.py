import requests, json


def taghcheh_sms(phone: str):
    phone = "0" + phone
    resp_sms = requests.post("https://gw.taaghche.com/v4/site/auth/login",
                             data=json.dumps(
                                 {"contact": phone, "forceOtp": False}),
                             headers={"Content-Type": "application/json"})

    print("Taghcheh_Done")
