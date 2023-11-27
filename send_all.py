import telebot
import sqlite_client

bot = telebot.TeleBot("6829297492:AAGAcsRcH0JsN46MpFj0VrW0dxJpG5FKmVk", parse_mode='HTML')


def send_all(message):
    users = sqlite_client.get_all_users()
    counter = 0
    for user in users:
        bot.send_message(user[0], f'Привет{", " + user[1] if user[1] else ""}\n{message}')
        counter += 1
        print(f'Прогресс {counter} / {len(users)}')



send_all(f'У нас хорошие скидки. Ай-да за покупками!')






