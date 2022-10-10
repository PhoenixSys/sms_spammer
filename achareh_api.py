import requests, json


def acharh_sms(phone: str):
    phone = "98" + phone
    resp_sms = requests.post("https://api.achareh.co/v2/accounts/login/",
                             data=json.dumps(
                                 {"phone": phone}),
                             headers={"Content-Type": "application/json"})
    try:
        status_sms = resp_sms.json()
        if status_sms['is_new']:
            print("Acahreh_Done")
            return True
        else:
            print("Acahreh_Failed")
            return False
    except Exception as e:
        print("Achareh_Failed")
        return False
