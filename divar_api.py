import requests, json


def divar_sms(phone: str):
    resp_sms = requests.post("https://api.divar.ir/v5/auth/authenticate",
                             data=json.dumps(
                                 {"phone": phone}),
                             headers={"Content-Type": "application/json"})
    try:
        status_sms = resp_sms.json()['authenticate_response']
        if status_sms == 'AUTHENTICATION_VERIFICATION_CODE_SENT':
            print("Divar_Done")
            return True
        else:
            print("Divar_Failed")
            return False
    except Exception as e:
        print("Divar_Failed")
        return False
