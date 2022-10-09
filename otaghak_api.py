import requests, json


def otaghak_sms(phone: str):
    phone = "0" + phone
    resp_sms = requests.post("https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode",
                             data=json.dumps(
                                 {"userName": phone}),
                             headers={"Content-Type": "application/json"})
    try:
        status_sms = resp_sms.json()
        if status_sms["cellPhoneNumber"] == phone:
            print("Otaghak_Done")
            return True
        else:
            print("Otaghak_Failed")
            return False
    except Exception as e:
        print("Otaghak_Failed")
        return False
