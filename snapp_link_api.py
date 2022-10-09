import requests, json


def snapp_link_sms(phone: str):
    phone = "0" + phone
    resp_sms = requests.post("https://api.snapp.ir/api/v1/sms/link",
                             data=json.dumps(
                                 {"phone": phone}),
                             headers={"Content-Type": "application/json"})
    try:
        status_sms = resp_sms.json()["status"]
        if status_sms == 200:
            print("Snapp_link_Done")
            return True
        else:
            print("Snapp_link_Failed")
            return False
    except Exception as e:
        print("Snapp_link_Failed")
        return False
