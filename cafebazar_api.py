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
    print("Caffe_bazar_Done")
