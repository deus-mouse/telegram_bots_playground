from pyrogram import Client, filters

app = Client("my_account")

# Эхо
@app.on_message(filters.me)
def echo(client, message):
    message.reply_text(message.text)

app.run()

