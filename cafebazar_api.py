import requests, json


def cafebazar_sms(phone: str):
    phone = "98" + phone
    resp_sms = requests.post("https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest",
                             data=json.dumps(
                                 {"properties": {"language": 1, "clientID": "dnux4qdirflddlgm3aziwbqh4va7ydb1",
                                                 "deviceID": "dnux4qdirflddlgm3aziwbqh4va7ydb1",
                                                 "clientVersion": "web"},
                                  "singleRequest": {"getOtpTokenRequest": {"username": phone}}}),
                             headers={"Content-Type": "application/json"})
    try:
        status_sms = resp_sms.json()["properties"]["statusCode"]
        if status_sms == 200:
            print("Caffe_bazar_Done")
            return True
        else:
            print("Caffe_bazar_Failed")
            return False
    except Exception as e:
        print("Caffe_bazar_Failed")
        return False
