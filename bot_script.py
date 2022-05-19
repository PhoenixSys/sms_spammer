import telebot
from telebot import types
from main import spammer
from datetime import datetime, timedelta

from mongo_db import DataBaseManagerUser

TOKEN = "5356098699:AAHLIDFeLmFcPsAL3VisFQiYjH_I21Xs4aw"
bot = telebot.TeleBot(token=TOKEN)

print("started !")


@bot.message_handler(commands=["start"])
def service1_command(message):
    bot.send_message(message.chat.id, f"Hello {message.from_user.first_name}")


@bot.message_handler(commands=["help"])
def help_func(message):
    bot.send_message(message.chat.id,
                     f"Welcome To Spammer Bot!\nIf You Want Use This Bot Please Send Message To @Eric_dev")
    bot.send_message(message.chat.id, "Example : \n9XXXXXXXXXXX\n2022-02-02 13:00:00\n2022-02-02 13:05:30")


@bot.message_handler(commands=["register"])
def service2_command(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Send phone",
                                        request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, 'Send Your Phone Number :', reply_markup=keyboard)


@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        if message.from_user.id == message.contact.user_id:
            if DataBaseManagerUser.insert_user_data(user_id=message.from_user.id, phone=message.contact.phone_number):
                bot.send_message(message.chat.id, f'Successful | {message.contact.phone_number} Registered')
            else:
                bot.send_message(message.chat.id, f'You Are Already Registered')
        else:
            bot.send_message(message.chat.id, 'Failed ! Please Send Your Own Number !')


@bot.message_handler()
def start_handler(message):
    user_id = message.from_user.id
    msg_content = message.text.split("\n")
    if msg_content[0] == "/admin":
        if user_id == 1727224717:
            command = msg_content[1]
            user_info = msg_content[2]
            if command == "add":
                DataBaseManagerUser.activator(user_id=user_info)
            elif command == "remove":
                DataBaseManagerUser.deactivator(user_id=user_info)
            bot.send_message(message.chat.id, "Done !")
        else:
            bot.send_message(message.chat.id, 'Only Admin Can Use This Command !')
    else:
        if DataBaseManagerUser.check_login(user_id=user_id):
            if user_id == 1727224717:
                bot.send_message(message.chat.id, "Started !")
                phone_number = msg_content[0]
                start_date = msg_content[1]
                end_date = msg_content[2]
                bot.send_message(message.chat.id, "Started !")
                spammer(phone_number, start_date, end_date)
                bot.send_message(message.chat.id, "Done !")
            else:
                phone_number = msg_content[0]
                start_date = str(datetime.strftime((datetime.now()), "%Y-%m-%d %H:%M:%S"))
                end_date = str(
                    datetime.strftime((datetime.now() + timedelta(minutes=1)), "%Y-%m-%d %H:%M:%S"))
                bot.send_message(message.chat.id, "Started !")
                spammer(phone_number, start_date, end_date)
                bot.send_message(message.chat.id, "Done !")
        else:
            bot.send_message(message.chat.id, 'You Are Not Allowed !!')


bot.polling()
