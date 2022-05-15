import requests, json


def sheypoor_sms(phone: str):
    phone = "0" + phone
    resp_sms = requests.post("https://www.sheypoor.com/api/v10.0.0/auth/send",
                             data=json.dumps(
                                 {"username": phone}),
                             headers={"Content-Type": "application/json",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    print("Sheypoor_Done")
