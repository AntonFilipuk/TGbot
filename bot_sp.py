import telebot
from telebot import types
import sqlite_client

bot = telebot.TeleBot("6829297492:AAGAcsRcH0JsN46MpFj0VrW0dxJpG5FKmVk", parse_mode='HTML')


@bot.message_handler(commands=['start'])
def handle_contact(message):
    # Создаем клаву
    keyboard = types.ReplyKeyboardMarkup()
    # Главный параметр здесь - request_contact - который запрашивает номер телефона
    button_phone = types.KeyboardButton(text="Отправить номер", request_contact=True)
    # Добавляем эту кнопку
    keyboard.add(button_phone)
    # Отправляем сообщение с клавой
    bot.send_message(message.chat.id, text='Укажите номер телефона', reply_markup=keyboard)


@bot.message_handler(content_types=['contact'])
def handle_phone(message):
    name = message.contact.first_name
    phone = message.contact.phone_number
    user_id = message.from_user.id
    username = message.from_user.username
    sqlite_client.save_user_to_db(user_id, phone, name, username)
    sqlite_client.get_all_users()

bot.infinity_polling()
