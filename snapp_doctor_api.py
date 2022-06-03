import requests
import json


def snapp_doctor_api(phone: str):
    resp_sms = requests.get(
        f"https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{phone}/sms?cCode=+98",
        headers={"Content-Type": "application/json",
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    try:
        status_sms = resp_sms.json()["result"]
        if status_sms != "ERROR":
            print("Snapp_Doctor_Done")
            return True
        else:
            print("Snapp_Doctor_Failed")
            return False
    except Exception as e:
        print(f"Snapp_Doctor_Failed, {e}")
        return False
