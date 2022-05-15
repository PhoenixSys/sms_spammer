import requests, json


def snapp_sms(phone: str):
    phone = "+98" + phone
    resp_sms = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
                             data=json.dumps(
                                 {"cellphone": phone}),
                             headers={"Content-Type": "application/json"})
    try:
        status_sms = resp_sms.json()["status"]
        if status_sms == "OK":
            print("Snapp_Done")
            return True
        else:
            print("Snapp_Failed")
            return False
    except Exception as e:
        print("Snapp_Failed")
        return False
