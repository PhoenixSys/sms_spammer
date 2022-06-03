import requests
import json


def talent_coach_api(phone: str):
    phone = "+98" + phone
    resp_sms = requests.post("https://rest.talentcoach.ir/api/v1/service/trainees/",
                             data=json.dumps(
                                 {"cellphone": phone}),
                             headers={"Content-Type": "application/json",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    try:
        status_sms = resp_sms.json()["expire_time"]
        if status_sms == 299:
            print("Talent_Coach_Done")
            return True
        else:
            print("Talent_Coach_Failed")
            return False
    except Exception as e:
        print(f"Talent_Coach_Failed, {e}")
        return False
