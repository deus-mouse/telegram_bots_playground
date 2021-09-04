from time import sleep

from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from bot.config import text as big_message

big_family_id = -282972466

me = 279478014
lena = 457526700
denis = 565712281

lanvin1392 = 430813324
p_chekhov = 100789680
MiraTyT = 500875961



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

target = big_family_id  # Target channel/supergroup

with app:
    for member in app.iter_chat_members(target):
        print(member.user.first_name)
        print(member.user.username)
        print(member.user.id)


app.run()

