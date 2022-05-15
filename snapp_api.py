import requests, json


def snapp_sms(phone: str):
    phone = "+98" + phone
    resp_sms = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
                             data=json.dumps(
                                 {"cellphone": phone}),
                             headers={"Content-Type": "application/json"})

    print("Snapp_Done")
