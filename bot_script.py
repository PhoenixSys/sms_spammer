import telebot
from main import spammer
from datetime import datetime, timedelta

TOKEN = "5356098699:AAHLIDFeLmFcPsAL3VisFQiYjH_I21Xs4aw"
bot = telebot.TeleBot(token=TOKEN)

print("started !")
users_allowed = [1727224717, 1056096689]


@bot.message_handler(commands=["start"])
def service1_command(message):
    bot.send_message(message.chat.id, f"Hello {message.from_user.first_name}")


@bot.message_handler(commands=["help"])
def help_func(message):
    bot.send_message(message.chat.id,
                     f"Welcome To Spammer Bot!\nIf You Want Use This Bot Please Send Message To @Eric_dev")
    bot.send_message(message.chat.id, "Example : \n9XXXXXXXXXXX\n2022-02-02 13:00:00\n2022-02-02 13:05:30")


@bot.message_handler()
def start_handler(message):
    user_id = message.from_user.id
    msg_content = message.text.split("\n")
    if msg_content[0] == "/admin":
        if user_id == 1727224717:
            command = msg_content[1]
            user_info = msg_content[2]
            if command == "add":
                users_allowed.append(int(user_info))
            elif command == "remove":
                users_allowed.remove(int(user_info))
            bot.send_message(message.chat.id, "Done !")
        else:
            bot.send_message(message.chat.id, 'Only Admin Can Use This Command !')
    else:
        if user_id in users_allowed:
            if user_id == 1727224717:
                phone_number = msg_content[1]
                start_date = msg_content[2]
                end_date = msg_content[3]
                spammer(phone_number, start_date, end_date)
                bot.send_message(message.chat.id, "Done !")
            else:
                phone_number = msg_content[1]
                start_date = str(datetime.strptime("{}".format(datetime.now()), "%Y-%m-%d %H:%M:%S"))
                end_date = str(
                    datetime.strptime("{}".format(datetime.now() + timedelta(minutes=1)), "%Y-%m-%d %H:%M:%S"))
                spammer(phone_number, start_date, end_date)
                bot.send_message(message.chat.id, "Done !")
        else:
            bot.send_message(message.chat.id, 'You Are Not Allowed !!')


bot.polling()
