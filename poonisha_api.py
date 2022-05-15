import requests, json


def poonisha_sms(phone: str):
    phone = "+98" + phone
    resp_sms = requests.post("https://ponisha.ir/send-mobile-verfication",
                             data=json.dumps(
                                 {"mobile": phone, "type": "1"}),
                             headers={"Content-Type": "application/json",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    print("Poonisha_SMS_Done")
    print("Poonisha_CALL_Done")


poonisha_sms("9142520208")
