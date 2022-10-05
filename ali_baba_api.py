import requests, json


def ali_baba(phone: str):
    resp_sms = requests.post("https://ws.alibaba.ir/api/v3/account/mobile/otp",
                             data=json.dumps(
                                 {"phoneNumber": phone}),
                             headers={"Content-Type": "application/json",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    resp_call = requests.post("https://ws.alibaba.ir/api/v3/account/call/otp",
                              data=json.dumps(
                                  {"phoneNumber": phone}),
                              headers={"Content-Type": "application/json",
                                       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    try:
        status_sms = resp_sms.json()["error"]
        status_call = resp_call.json()["error"]
        if status_sms == None and status_call == None:
            print("Ali_baba_Done")
            return True
        else:
            print("Ali_baba_Failed")
            return False
    except Exception as e:
        print("Ali_baba_Failed")
        return False
