import telebot
from telebot import types
from main import spammer
from datetime import datetime, timedelta

from mongo_db import DataBaseManagerUser

TOKEN = "5356098699:AAHLIDFeLmFcPsAL3VisFQiYjH_I21Xs4aw"
bot = telebot.TeleBot(token=TOKEN)

print("started !")


def target_phone_number_validation(phone_number):
    if len(phone_number) == 10:
        if phone_number[0] == '9':
            return True
    return False


@bot.message_handler(commands=["start"])
def service1_command(message):
    if message.chat.id == 1727224717:
        bot.send_message(message.chat.id, f"Hello Dear Admin")
    else:
        bot.send_message(message.chat.id, f"Hello {message.from_user.first_name}")


@bot.message_handler(commands=["help"])
def help_func(message):
    bot.send_message(message.chat.id,
                     f"Welcome To Spammer Bot!\nIf You Want To Use This Bot ---> /register .")
    if message.chat.id == 1727224717:
        bot.send_message(message.chat.id, "Example : \n9XXXXXXXXXXX\n1")
    else:
        bot.send_message(message.chat.id, "Example : \n9XXXXXXXXXXX")


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
                bot.send_message(1727224717,
                                 f'Phone : {message.contact.phone_number} \nId : {message.chat.id} \nRegistered')
            else:
                bot.send_message(message.chat.id, f'You Are Already Registered')
        else:
            bot.send_message(message.chat.id, 'Failed ! Please Send Your Own Number !')


@bot.message_handler(commands=["users_list"])
def users_list(message):
    user_id = message.from_user.id
    if DataBaseManagerUser.check_login(user_id):
        if user_id == 1727224717:
            msg = ""
            for user in DataBaseManagerUser.users_list():
                msg += f"Phone : {user['phone']}\nUser_id : {user['user_id']}\nStatus : {user['status']}\n\n"
            bot.send_message(message.chat.id, msg)
        else:
            bot.send_message(message.chat.id, 'Only Admin Can Use This Command !')
    else:
        bot.send_message(message.chat.id, 'You Are Not Registered !')


@bot.message_handler()
def start_handler(message):
    user_id = message.from_user.id
    msg_content = message.text.split("\n")
    if msg_content[0] == "/admin":
        if user_id == 1727224717:
            command = msg_content[1]
            if command == "add":
                content = msg_content[2]
                if DataBaseManagerUser.activator(user_id=int(content)):
                    bot.send_message(int(content), f"YOU CAN USE THIS BOT NOW !")
                    bot.send_message(message.chat.id, f"{int(content)} Activated")
                else:
                    bot.send_message(message.chat.id, f"{int(content)} Failed")
            elif command == "remove":
                content = msg_content[2]
                if DataBaseManagerUser.deactivator(user_id=int(content)):
                    bot.send_message(int(content), f"YOU CAN NOT USE THIS BOT NOW !")
                    bot.send_message(message.chat.id, f"{int(content)} Deactivated")
                else:
                    bot.send_message(message.chat.id, f"{int(content)} Failed")
            elif command == "remove_all":
                for user in DataBaseManagerUser.users_list():
                    if int(user['user_id']) != 1727224717:
                        DataBaseManagerUser.deactivator(user_id=int(user['user_id']))
                bot.send_message(message.chat.id, f"All Users Deactivated !")
            elif command == "push_notification":
                content = msg_content[2]
                for user in DataBaseManagerUser.users_list():
                    if int(user['user_id']) != 1727224717:
                        bot.send_message(int(user['user_id']), content)
                bot.send_message(message.chat.id, f"Notifications Sent")
            else:
                bot.send_message(message.chat.id, 'Wrong Command !')
        else:
            bot.send_message(message.chat.id, 'Only Admin Can Use This Command !')
    else:
        if DataBaseManagerUser.check_login(user_id=user_id):
            if user_id == 1727224717:
                phone_number = msg_content[0]
                period = msg_content[1]
                start_date = str(datetime.strftime((datetime.now()), "%Y-%m-%d %H:%M:%S"))
                end_date = str(
                    datetime.strftime((datetime.now() + timedelta(minutes=int(period))), "%Y-%m-%d %H:%M:%S"))
                if target_phone_number_validation(phone_number):
                    bot.send_message(message.chat.id, "Started !")
                    bot.send_message(1727224717,
                                     f"USER_ID : {user_id} \nSTART ATTACK ON : {phone_number}")
                    spammer(phone_number, start_date, end_date)
                    bot.send_message(message.chat.id, "Done !")
                else:
                    bot.send_message(message.chat.id, "Phone Number Is Wrong !")
            else:
                phone_number = msg_content[0]
                if str(phone_number) != "9142520208":
                    start_date = str(datetime.strftime((datetime.now()), "%Y-%m-%d %H:%M:%S"))
                    end_date = str(
                        datetime.strftime((datetime.now() + timedelta(minutes=1)), "%Y-%m-%d %H:%M:%S"))
                    if target_phone_number_validation(phone_number):
                        bot.send_message(message.chat.id, "Started !")
                        bot.send_message(1727224717,
                                         f"USER_ID : {user_id} \nSTART ATTACK ON : {phone_number}")
                        spammer(phone_number, start_date, end_date)
                        bot.send_message(message.chat.id, "Done !")
                    else:
                        bot.send_message(message.chat.id, "Phone Number Is Wrong !")
                else:
                    DataBaseManagerUser.deactivator(user_id=int(user_id))
                    bot.send_message(message.chat.id, "No No Noooo :)")
                    bot.send_message(message.chat.id, f"YOU CAN NOT USE THIS BOT NOW !")
        else:
            bot.send_message(message.chat.id, 'You Are Not Allowed !!')


bot.polling()
