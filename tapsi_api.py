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
    print(resp_sms.json())
    print(resp_call.json())
# {"credential":{"phoneNumber":"09142520208","role":"PASSENGER"},"otpOption":"ROBO_CALL"}
# {"credential":{"phoneNumber":"09142520208","role":"PASSENGER"},"otpOption":"SMS"}
