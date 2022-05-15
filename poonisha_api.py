import requests, json


def poonisha_sms(phone: str):
    phone = "+98" + phone
    resp_sms = requests.post("https://ponisha.ir/send-mobile-verfication",
                             data=json.dumps(
                                 {"mobile": phone, "type": "1"}),
                             headers={"Content-Type": "application/json",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    resp_call = requests.post("https://ponisha.ir/send-mobile-verfication",
                              data=json.dumps(
                                  {"mobile": phone, "type": "2"}),
                              headers={"Content-Type": "application/json",
                                       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    try:
        status_sms = resp_sms.json()["status"]
        status_call = resp_call.json()["status"]
        if status_sms == "created":
            print("Poonisha_SMS_Done")
        else:
            print("Poonisha_SMS_Failed")
        if status_call == "exists":
            print("Poonisha_CALL_Done")
        else:
            print("Poonisha_CALL_Failed")
    except Exception as e:
        print("Poonisha_SMS_Failed")
        print("Poonisha_CALL_Failed")
