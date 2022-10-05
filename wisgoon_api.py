import requests, json


def wisgoon_sms(phone: str):
    phone = "0" + phone
    resp_sms = requests.post("https://chamedoon.com/api/v1/membership/guest/request_mobile_verification",
                             data=json.dumps(
                                 {"mobile": phone, "origin": "/", "referrer_id": None}),
                             headers={"Content-Type": "application/json"})
    try:
        status_sms = resp_sms.json()["status"]
        if status_sms == "ok":
            print("Wisgoon_Done")
            return True
        else:
            print("Wisgoon_Failed")
            return False
    except Exception as e:
        print("Wisgoon_Failed")
        return False
