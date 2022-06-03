import requests
import json


def doctor_to_sms(phone: str):
    resp_sms = requests.post("https://api.doctoreto.com/api/web/patient/v1/accounts/register",
                             data=json.dumps(
                                 {"mobile": phone, "country_id": 205}),
                             headers={"Content-Type": "application/json",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    try:
        status_sms = resp_sms.json()["errors"]
        if status_sms is None:
            print("Doctor_To_Done")
            return True
        else:
            print("Doctor_To_Failed")
            return False
    except Exception as e:
        print(f"Doctor_To_Failed, {e}")
        return False
