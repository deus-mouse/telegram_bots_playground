# - *- coding: utf- 8 - *-
import json

import telebot
import subprocess
import config
import re

me = 279478014
lena = 457526700


text = config.text
bot = telebot.TeleBot(config.bot_token)

@bot.message_handler(content_types=["text"])
def voice_handler(message):
    if message.text == "го":
        print("отправляем")
        bot.send_message(279478014, text)
        print("отправили")

bot.polling(none_stop=True)
