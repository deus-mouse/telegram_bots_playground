# - *- coding: utf- 8 - *-



import telebot
import config



text = config.text
bot = telebot.TeleBot(config.ed_bot_token)

@bot.message_handler(content_types=["text"])
def text_handler(message):

    # дергает id группы
    if message.text == "id":
        # print("отправляем")
        # bot.send_message(me, text)
        # print("отправили")
        print("message.chat.id", message.chat.id)
        bot.send_message(message.chat.id, f"id группы {message.chat.id}", reply_to_message_id=message.message_id)

bot.polling(none_stop=True)
