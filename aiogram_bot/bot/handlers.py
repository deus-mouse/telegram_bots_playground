from aiogram_bot.bot.instances import *
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


async def on_startup(_):
    print("I'm alive")


# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    # await message.reply(text=text_storage.help, parse_mode='HTML')
    await bot.send_message(chat_id=message.from_user.id,
                           text=text_storage.help,
                           parse_mode='HTML',
                           reply_markup=ReplyKeyboardRemove()
                           )
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # await message.answer(text=text_storage.start,
    #                      reply_markup=kb,
    #                      )
    await bot.send_message(chat_id=message.from_user.id, text=text_storage.start, reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['description'])
async def start_command(message: types.Message):
    await message.answer(text=text_storage.description)
    await message.delete()


@dp.message_handler(commands=['description'])
async def start_command(message: types.Message):
    await message.answer(text=text_storage.description)
    await message.delete()


@dp.message_handler(commands=['give'])
async def send_sticker(message: types.Message):
    await message.answer('Лови 😜')
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEHtDtj6OrSH_uaky0-ikRMS-3IL29hkwACEwADqXxOEV9V_IEdyyrpLgQ')
    await message.delete()


@dp.message_handler(content_types=['sticker'])
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)
    await message.delete()


@dp.message_handler(commands=['image'])
async def send_photo_(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://images.mubicdn.net/images/film/26742/cache-128101-1498177959/image-w1280.jpg?size=800x")
    await message.delete()


@dp.message_handler(commands=['location'])
async def send_location_(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id, latitude=44.761182, longitude=20.505305)
    await message.delete()




