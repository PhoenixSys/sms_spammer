import requests, json


def alopeyk_sms(phone: str):
    phone = "0" + phone
    resp_sms = requests.post("https://api.alopeyk.com/api/v2/login?platform=pwa",
                             data=json.dumps(
                                 {"type": "CUSTOMER", "model": "Chrome 106.0.0.0", "platform": "pwa", "version": "10",
                                  "manufacturer": "Windows", "isVirtual": False, "serial": True, "app_version": "1.2.7",
                                  "uuid": True, "phone": phone}),
                             headers={"Content-Type": "application/json"})
    try:
        status_sms = {"status": "success", "message": None,
                      "object": {"token": "DRBMN6X59NBD49H9BZ5SCLS8B76RDKXMKSRLFH7F5XDDHB1N5RM2DKZM3MLNCXHS"}}
        if status_sms["status"] == "success":
            print("Alopeyk_Done")
            return True
        else:
            print("Alopeyk_Failed")
            return False
    except Exception as e:
        print("Alopeyk_Failed")
        return False



