import io
import math
import os.path
import sys

import requests
import telebot
from PIL import Image

from models_code.make_prediction import predicted_age, decode

token = 'ENTER YOUR TOKEN HERE'
bot = telebot.TeleBot(token)
URI_INFO = f"https://api.telegram.org/bot{token}/getfile?file_id="
URI = f"https://api.telegram.org/file/bot{token}/"


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.from_user.id,
                     """Welcome to the AgeDetection Bot! 👋  
This bot uses advanced algorithms to estimate the age of individuals from photos. Here's how you can get started:

📸 Send me a clear photo of a face, and I'll estimate the age for you.

ℹ️ For more information, type /help.

                     """)


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.from_user.id,
                     """
                     📖 AgeDetection Bot - Help Menu

🤔 **What can I do?**
- Send a clear photo of a face, and I’ll analyze it to estimate the age.

📋 **Commands you can use:**
- `/start` - Show the welcome message.
- `/help` - Display this help menu.

📌 **Tips for best results:**
- Ensure the photo is clear and well-lit.
- The face should be directly facing the camera.
- Avoid group photos or blurry images.
- The better the photo quality, the more accurate the prediction. Try it now!
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
    bot.send_message(message.from_user.id, get_predicted_age(img_path, model_name='CNNClassificationModel.pt'))
    os.remove(img_path)


def get_predicted_age(img_path, model_name):
    age1 = predicted_age(img_path, model_name)
    age2 = predicted_age(img_path, model_name)
    age3 = predicted_age(img_path, model_name)
    return decode[math.floor((age1 + age2 + age3) / 3)]


bot.infinity_polling()
