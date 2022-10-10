import telebot
from telebot import types
from main import spammer
from datetime import datetime, timedelta
from mongo_db import DataBaseManagerUser

TOKEN = "5356098699:AAHLIDFeLmFcPsAL3VisFQiYjH_I21Xs4aw"
bot = telebot.TeleBot(token=TOKEN)

print("started !")

admin_user_id = 1727224717


def target_phone_number_validation(phone_number):
    if len(phone_number) == 10:
        if phone_number[0] == '9':
            return True
    return False


@bot.message_handler(commands=["start"])
def service1_command(message):
    if message.chat.id == admin_user_id:
        bot.send_message(message.chat.id, f"Hello Dear Admin")
    else:
        bot.send_message(message.chat.id, f"Hello {message.from_user.first_name}")


@bot.message_handler(commands=["help"])
def help_func(message):
    bot.send_message(message.chat.id,
                     f"Welcome To Spammer Bot!\nIf You Want To Use This Bot ---> /register .")
    if message.chat.id == admin_user_id:
        bot.send_message(message.chat.id,
                         "commands :\nactivate\ndeactivate\nactivate_all\ndeactivate_all\nset_vip\nunset_vip\npush_notification\nusers_list")
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
                bot.send_message(admin_user_id,
                                 f'Phone : {message.contact.phone_number} \nId : {message.chat.id} \nRegistered')
            else:
                bot.send_message(message.chat.id, f'You Are Already Registered')
        else:
            bot.send_message(message.chat.id, 'Failed ! Please Send Your Own Number !')


@bot.message_handler(commands=["users_list"])
def users_list(message):
    user_id = message.from_user.id
    if user_id == admin_user_id:
        msg = ""
        counter = 0
        for user in DataBaseManagerUser.users_list():
            counter += 1
            msg += f"Phone : {user['phone']}\nUser_id : {user['user_id']}\nStatus : {user['status']}\nVip : {user['vip']}\nSpam Count : {user['spam_count']}\n\n"
        msg += f"Total Users : {counter}"
        bot.send_message(message.chat.id, msg)
    else:
        bot.send_message(message.chat.id, 'Only Admin Can Use This Command !')


@bot.message_handler()
def start_handler(message):
    user_id = message.from_user.id
    msg_content = message.text.split("\n")
    if msg_content[0] == "/admin":
        if user_id == admin_user_id:
            command = msg_content[1].lower()
            if command == "activate":
                content = msg_content[2]
                if DataBaseManagerUser.activator(user_id=int(content)):
                    bot.send_message(int(content), f"YOU CAN USE THIS BOT NOW !")
                    bot.send_message(message.chat.id, f"{int(content)} Activated")
                else:
                    bot.send_message(message.chat.id, f"{int(content)} Failed")
            elif command == "deactivate":
                content = msg_content[2]
                if DataBaseManagerUser.deactivator(user_id=int(content)):
                    bot.send_message(int(content), f"SORRY ! YOU CAN NOT USE THIS BOT !")
                    bot.send_message(message.chat.id, f"{int(content)} Deactivated")
                else:
                    bot.send_message(message.chat.id, f"{int(content)} Failed")
            elif command == "deactivate_all":
                for user in DataBaseManagerUser.users_list():
                    if int(user['user_id']) != admin_user_id:
                        try:
                            DataBaseManagerUser.deactivator(user_id=int(user['user_id']))
                            bot.send_message(int(user['user_id']), f"YOU CAN NOT USE THIS BOT NOW !")
                        except Exception as e:
                            bot.send_message(message.chat.id, f"Error : {e} !")
                bot.send_message(message.chat.id, f"All Users Deactivated !")
            elif command == "activate_all":
                for user in DataBaseManagerUser.users_list():
                    if int(user['user_id']) != admin_user_id:
                        try:
                            DataBaseManagerUser.activator(user_id=int(user['user_id']))
                            bot.send_message(int(user['user_id']), f"YOU CAN USE THIS BOT NOW !")
                        except Exception as e:
                            bot.send_message(message.chat.id, f"Error : {e} !")
                bot.send_message(message.chat.id, f"All Users Activated !")
            elif command == "set_vip":
                content = msg_content[2]
                if DataBaseManagerUser.set_vip(user_id=int(content)):
                    bot.send_message(message.chat.id, f"{int(content)} Add To Vip")
                else:
                    bot.send_message(message.chat.id, f"{int(content)} Failed")
            elif command == "unset_vip":
                content = msg_content[2]
                if DataBaseManagerUser.unset_vip(user_id=int(content)):
                    bot.send_message(message.chat.id, f"{int(content)} Removed From Vip")
                else:
                    bot.send_message(message.chat.id, f"{int(content)} Failed")
            elif command == "push_notification":
                content = msg_content[2]
                for user in DataBaseManagerUser.users_list():
                    if int(user['user_id']) != admin_user_id:
                        try:
                            bot.send_message(int(user['user_id']), content)
                        except Exception as e:
                            bot.send_message(message.chat.id, f"Error : {e} !")
                bot.send_message(message.chat.id, f"Notifications Sent")
            else:
                bot.send_message(message.chat.id, 'Wrong Command !')
        else:
            bot.send_message(message.chat.id, 'Only Admin Can Use This Command !')
    else:
        if DataBaseManagerUser.check_login(user_id=user_id) and (
                DataBaseManagerUser.spam_count(user_id=user_id) <= 3 or DataBaseManagerUser.check_vip(
            user_id=user_id) == True):
            if user_id == admin_user_id:
                phone_number = msg_content[0]
                period = msg_content[1]
                end_time = str(
                    datetime.strftime((datetime.now() + timedelta(minutes=int(period))), "%Y-%m-%d %H:%M:%S"))
                if target_phone_number_validation(phone_number):
                    bot.send_message(message.chat.id, "Started !")
                    DataBaseManagerUser.spam_count_up(user_id=user_id)
                    bot.send_message(admin_user_id,
                                     f"USER_ID : {user_id} \nSTART ATTACK ON : {phone_number}")
                    spammer(phone_number, end_time, message.chat.id)
                else:
                    bot.send_message(message.chat.id, "Phone Number Is Wrong !")
            else:
                phone_number = msg_content[0]
                if str(phone_number) != "9142520208":
                    end_time = str(
                        datetime.strftime((datetime.now() + timedelta(minutes=10)), "%Y-%m-%d %H:%M:%S"))
                    if target_phone_number_validation(phone_number):
                        bot.send_message(message.chat.id, "Started !")
                        DataBaseManagerUser.spam_count_up(user_id=user_id)
                        bot.send_message(admin_user_id,
                                         f"USER_ID : {user_id} \nSTART ATTACK ON : {phone_number}")
                        spammer(phone_number, end_time, message.chat.id)
                    else:
                        bot.send_message(message.chat.id, "Phone Number Is Wrong !")
                else:
                    DataBaseManagerUser.deactivator(user_id=int(user_id))
                    bot.send_message(message.chat.id, "No No Noooo :)")
                    bot.send_message(message.chat.id, f"SORRY ! YOU CAN NOT USE THIS BOT NOW !")
        else:
            bot.send_message(message.chat.id, 'You Are Not Allowed !!')


bot.polling(non_stop=True, interval=0)
