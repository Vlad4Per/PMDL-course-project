import io
import math
import os.path
import sys

import requests
import telebot
from PIL import Image

from models.make_prediction import predicted_age, decode

token = '8148288527:AAH1XAXhvgdVPurjT1t0bhqMsB5xT0C1QLk'
bot = telebot.TeleBot(token)
URI_INFO = f"https://api.telegram.org/bot{token}/getfile?file_id="
URI = f"https://api.telegram.org/file/bot{token}/"


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.from_user.id, "This is an AgeDetectionBot")


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.from_user.id,
                     """
                     ...some info...\nto start write /start command
                     """)


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.from_user.id, "I don't understand what you say...")
    help_command(message)


@bot.message_handler(content_types=['photo'])
def image(message):
    file_id = message.photo[-1].file_id
    img_path = requests.get(URI_INFO + file_id).json()['result']['file_path']
    img = Image.open(io.BytesIO(requests.get(URI + img_path).content))
    if not os.path.exists('static'):
        os.makedirs('static')
    img_path = f'static/{file_id}.png'
    img.save(img_path, format='PNG')
    bot.send_message(message.from_user.id, get_predicted_age(img_path))
    os.remove(img_path)


def get_predicted_age(img_path):
    age1 = predicted_age(img_path)
    age2 = predicted_age(img_path)
    age3 = predicted_age(img_path)
    return decode[math.floor((age1 + age2 + age3) / 3)]


bot.infinity_polling()
