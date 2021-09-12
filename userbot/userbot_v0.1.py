from time import sleep

from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from data import *

app = Client("my_account")

# Эхо
# @app.on_message(filters.me)
# def echo(client, message):
#     print(message.text)
#     message.reply_text(message.text)

# Команда type
# @app.on_message(filters.command("type", prefixes=".") & filters.me)
# def type(client, msg):
#     orig_text = msg.text.split(".type ", maxsplit=1)[1]
#     text = orig_text
#     tbp = ""  # to be printed
#     typing_symbol = "▓"
#
#     while(tbp != orig_text):
#         try:
#             msg.edit(tbp + typing_symbol)
#             sleep(0.05) # 50 ms
#             tbp = tbp + text[0]
#             text = text[1:]
#
#             msg.edit(tbp)
#             sleep(0.05)
#
#         except FloodWait as e:
#             print("FloodWait", e.x)
#             sleep(e.x)


# with app:
#     # Send a message, Markdown is enabled by default
#     # app.send_message("me", "Hi there! I'm using **Pyrogram**")
#     app.send_message(p_chekhov, big_message)
#     # Send a location
#     # app.send_location("me", 51.500729, -0.124583)
#
#     # Send a sticker
#     # app.send_sticker("me", "CAADBAADzg4AAvLQYAEz_x2EOgdRwBYE")


# Get all the members of a chat.
target = infra_chat_id  # Target channel/supergroup
with app:

    # присылает список имен, ников и id из чата
    # for member in app.iter_chat_members(target):
    #     app.send_message(chat_id=infra_chat_id, text=str(member.user.first_name))
    #     print(member.user.first_name, type(member.user.first_name))
    #     # app.send_message(me, text=str(member.user.first_name))
    #     app.send_message(chat_id=infra_chat_id, text=str(member.user.username))
    #     print(member.user.username, type(member.user.username))
    #     # app.send_message(me, text=str(member.user.username))
    #     app.send_message(chat_id=infra_chat_id, text=str(member.user.id))
    #     print(member.user.id, type(member.user.id))
    #     # app.send_message(me, text=str(member.user.id))
    #     app.send_message(chat_id=infra_chat_id, text="xxxxxxxxxxxxxxxx")
    #     print("xxxxxxxxxxxxxxxx")
    #     # app.send_message(me, text="xxxxxxxxxxxxxxxx")

    # добавляет в контакты
    for user in another_contacts:
        for username, id in user.items():
            print(username, id)
            app.add_contact(id, username)
            # app.send_message(chat_id=id, text=message_to_send)

app.run()

