from retrolan_bot.bot.instances import *
from aiogram.types import ReplyKeyboardRemove


async def on_startup(_):
    print("I'm alive")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=text_storage.help,
                           parse_mode='HTML',
                           reply_markup=ReplyKeyboardRemove()
                           )
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=text_storage.start)
    await message.delete()
    await message.answer(text='/start_survey чтобы начать опрос')


@dp.message_handler(commands=['start_survey'])
async def links_command(message: types.Message):
    survey.switch = True
    await message.delete()
    await message.answer(survey.next_question())


@dp.message_handler(content_types=['text'])
async def send_sticker_id(message: types.Message):
    if survey.switch:
        survey.update_answers(message.text)
        question = survey.next_question()
        if question:
            await message.answer(question)
        else:
            survey.switch = False
            await bot.send_message(chat_id=id_storage['говорящий_гараж'], text=survey.send(), parse_mode='HTML')
            await message.answer('Я подумаю, посовещаюсь с гаражниками, и дам свой ответ 🤖')


