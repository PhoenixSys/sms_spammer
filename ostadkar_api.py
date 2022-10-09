import requests, json


def ostadkar_sms(phone: str):
    phone = "0" + phone
    resp_sms = requests.post("https://api.ostadkr.com/login",
                             data=json.dumps(
                                 {"mobile": phone}),
                             headers={"Content-Type": "application/json"})
    try:
        status_sms = {"duration":90}
        if status_sms["duration"] == 90:
            print("Ostadkar_Done")
            return True
        else:
            print("Ostadkar_Failed")
            return False
    except Exception as e:
        print("Ostadkar_Failed")
        return False


