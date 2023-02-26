from retrolan_bot.bot.instances import *
from aiogram.types import ReplyKeyboardRemove


async def on_startup(_):
    print("I'm alive")


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
    await bot.send_message(chat_id=message.from_user.id, text=text_storage.start,
                           # reply_markup=kb
                           )
    await message.delete()
    await message.answer(text='заполните, пожалуйста, форму', reply_markup=ikb)



@dp.message_handler(commands=['links'])
async def links_command(message: types.Message):
    '''вызывыет inline-keyboard'''
    await message.answer(text='choose option...', reply_markup=ikb)




