import requests, json


def mobit_sms(phone: str):
    phone = "0" + phone
    resp_sms = requests.post("https://api.mobit.ir/api/web/v8/register/register",
                             data=json.dumps(
                                 {"number": phone}
                                 ),
                             headers={"Content-Type": "application/json"})
    try:
        status_sms = resp_sms.json()
        if status_sms['success']:
            print("mobit_Done")
            return True
        else:
            print("mobit_Failed")
            return False
    except Exception as e:
        print("mobit_Failed")
        return False


if __name__ == '__main__':
    mobit_sms("9182251753")
