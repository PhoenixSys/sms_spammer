import requests, json


def digikala_sms(phone: str):
    phone = "0" + phone
    resp_sms = requests.post("https://api.digikala.com/v1/user/authenticate/",
                             data=json.dumps(
                                 {"backUrl": "/", "username": phone, "otp_call": False}),
                             headers={"Content-Type": "application/json",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    try:
        status_sms = resp_sms.json()["status"]
        if status_sms == 200:
            print("Digi_kala_Done")
            return True
        else:
            print("Digi_kala_Failed")
            return False
    except Exception as e:
        print("Digi_kala_Failed")
        return False
