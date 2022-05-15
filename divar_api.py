import requests, json


def divar_sms(phone: str):
    resp_sms = requests.post("https://api.divar.ir/v5/auth/authenticate",
                             data=json.dumps(
                                 {"phone": phone}),
                             headers={"Content-Type": "application/json"})

    print("Divar_Done")
