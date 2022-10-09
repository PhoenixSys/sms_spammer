import requests, json


def kilid_sms(phone: str):
    phone = "0" + phone
    resp_sms = requests.post(
        "https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL",
        data=json.dumps(
            {"mobile": phone}),
        headers={"Content-Type": "application/json"})
    try:
        status_sms = resp_sms.json()['status']
        if status_sms == 'SUCCESS':
            print("kilid_Done")
            return True
        else:
            print("kilid_Failed")
            return False
    except Exception as e:
        print("kilidk_Failed")
        return False
