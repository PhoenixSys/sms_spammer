import requests
import json


def gapofilm_api(phone: str):
    resp_sms = requests.post(
        "https://core.gapfilm.ir/api/v3.1/Account/Login",
        data=json.dumps(
            {"Type": 3, "Username": phone, "SourceChannel": "GF_WebSite", "SourcePlatform": "desktop",
             "SourcePlatformAgentType": "Chrome", "SourcePlatformVersion": "96.0.4664.93", "GiftCode": None}),
        headers={"Content-Type": "application/json",
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    try:
        status_sms = resp_sms.json()["Code"]
        if status_sms == 1:
            print("GapoFilm_Done")
            return True
        else:
            print("GapoFilm_Failed")
            return False
    except Exception as e:
        print(f"GapoFilm_Failed, {e}")
        return False
