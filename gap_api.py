import requests, json


def gap(phone: str):
    phone = "98" + phone
    resp_sms = requests.post(" https://core.gap.im/v1/user/add.json?mobile=%2B{}".format(phone),
                             headers={"Content-Type": "application/json"})
    resp_call = requests.post(f"https://core.gap.im/v1/user/resendCode.json?mobile=%2B{phone}&type=IVR",
                              headers={"Content-Type": "application/json"})
    try:
        status_sms = resp_sms.json()["status"]
        status_call = resp_call.json()["status"]
        if status_sms == "success" and status_call == "success":
            print("Gap_Done")
        else:
            print("Gap_Failed")
            return False
    except Exception as e:
        print("Gap_Failed")
        return False
