import requests, json


def malltina_sms(phone: str):
    phone = "0" + phone
    resp_sms = requests.post("https://api.malltina.com/profiles",
                             data=json.dumps(
                                 {"password": "akbar1234", "mobile": phone, "first_name": "akbar"}),
                             headers={"Content-Type": "application/json"})
    try:
        status_sms = resp_sms.json()['status']
        if status_sms == "success":
            print("Malltina_Done")
            return True
        else:
            print("Malltina_Failed")
            return False
    except Exception as e:
        print("Malltina_Failed")
        return False
