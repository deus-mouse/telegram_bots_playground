# - *- coding: utf- 8 - *-

import telebot
import config

me = 279478014
lena = 457526700


text = config.text
bot = telebot.TeleBot(config.bot_token)

@bot.message_handler(content_types=["text"])
def text_handler(message):
    if message.text == "Дай id этой группы":
        # print("отправляем")
        # bot.send_message(me, text)
        # print("отправили")
        print("message.chat.id", message.chat.id)
        bot.send_message(message.chat.id, f"id группы {message.chat.id}", reply_to_message_id=message.message_id)

bot.polling(none_stop=True)
