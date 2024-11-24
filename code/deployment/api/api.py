import io
from PIL import Image

import requests
import telebot

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
    print(img.size)


bot.infinity_polling()
