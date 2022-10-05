import requests, json


def pinket_sms(phone: str):
    phone = "0" + phone
    resp_sms = requests.post("https://pinket.com/api/cu/v2/phone-verification",
                             data=json.dumps(
                                 {"phoneNumber": phone}),
                             headers={"Content-Type": "application/json"})
    print("Pinket_Done")
    return True
