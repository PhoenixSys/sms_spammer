import requests
import json


def fitamin_api(phone: str):
    phone = "98" + phone
    resp_sms = requests.get(
        f"https://behandam.kermany.com/fitamin-central-service/api/fitamin/v2/register/status?mobile={phone}",
        headers={"Content-Type": "application/json",
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    try:
        status_sms = resp_sms.json()["error"]["errors"]
        if status_sms is None:
            print("Fitamin_Done")
            return True
        else:
            print("Fitamin_Failed")
            return False
    except Exception as e:
        print(f"Fitamin_Failed, {e}")
        return False
