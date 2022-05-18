import time
import os
from datetime import datetime, timedelta
from cafebazar_api import cafebazar_sms
from digikala_api import digikala_sms
from divar_api import divar_sms
from sheypoor_api import sheypoor_sms
from snapp_api import snapp_sms
from tapsi_api import tapsi_sms_call
from poonisha_api import poonisha_sms
from taghcheh_api import taghcheh_sms

phone = input("Enter target phone number (example : 9XXXXXXXXXXX) : ")
schedule = input("Enter schedule time (example : 2022-05-11 13:00:00) : ")
end_schedule = input("Enter end schedule time (example : 2022-02-02 13:05:30) : ")

if schedule.strip() == "":
    schedule = datetime.now()
schedule_date_time_obj = datetime.strptime("{}".format(schedule), "%Y-%m-%d %H:%M:%S")
end_schedule_date_time_obj = datetime.strptime("{}".format(end_schedule), "%Y-%m-%d %H:%M:%S")

while True:
    if datetime.now() > schedule_date_time_obj:
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Waiting for schedule time...")
        print("Current time : {}".format(datetime.now()))
        print("Schedule time : {}".format(schedule_date_time_obj))
        time.sleep(1)

while end_schedule_date_time_obj > datetime.now():
    cafebazar_sms(phone)
    digikala_sms(phone)
    divar_sms(phone)
    sheypoor_sms(phone)
    snapp_sms(phone)
    tapsi_sms_call(phone)
    poonisha_sms(phone)
    taghcheh_sms(phone)
