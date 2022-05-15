import requests, json


def tapsi_sms_call(phone: str):
    phone = "0" + phone
    resp_sms = requests.post("https://api.tapsi.cab/api/v2.2/user",
                             data=json.dumps(
                                 {"credential": {"phoneNumber": phone, "role": "PASSENGER"}, "otpOption": "SMS"}),
                             headers={"Content-Type": "application/json"})
    resp_call = requests.post("https://api.tapsi.cab/api/v2.2/user",
                              data=json.dumps(
                                  {"credential": {"phoneNumber": phone, "role": "PASSENGER"},
                                   "otpOption": "ROBO_CALL"}),
                              headers={"Content-Type": "application/json"})
    try:
        status_sms = resp_sms.json()["result"]
        status_call = resp_call.json()["result"]
        if status_sms == "OK":
            print("Tapsi_SMS_Done")
        else:
            print("Tapsi_SMS_Failed")
        if status_call == "OK":
            print("Tapsi_Call_Done")
        else:
            print("Tapsi_Call_Failed")
    except Exception as e:
        print("Tapsi_SMS_Failed")
        print("Tapsi_Call_Failed")
