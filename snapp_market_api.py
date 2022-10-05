import requests, json


def snapp_market_sms(phone: str):
    phone = "0" + phone
    resp_sms = requests.post("https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={}".format(phone),
                             headers={"Content-Type": "application/json"})
    try:
        status_sms = resp_sms.json()["status"]
        if status_sms == True:
            print("Snapp_Market_Done")
            return True
        else:
            print("Snapp_Market_Failed")
            return False
    except Exception as e:
        print("Snapp_Market_Failed")
        return False
