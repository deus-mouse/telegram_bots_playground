from instances import *


async def survey_flow(message):
    '''
    message.from_user.url = tg://user?id=457526700
    message.chat.id = 457526700
    :param message:
    :return:
    '''
    for index in range(len(surveys_holder)):
        survey = surveys_holder[index]
        if survey.id == message.from_user.id and survey.switch:
            survey.update_answers(message.text)
            question = survey.next_question()
            if question:
                logging.debug(f'{message.from_user.id}: {question}')
                print(f'{message.from_user.id}: {question}')
                await message.answer(question)
            else:
                # survey.switch = False
                button_url = message.from_user.url
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(text=message.from_user.username, url=button_url))
                await bot.send_message(id_storage['говорящий_гараж'], text=survey.send(), parse_mode='HTML',
                                       reply_markup=markup)
                await message.answer('Я подумаю, посовещаюсь с гаражниками, и дам свой ответ 🤖')
                surveys_complete_holder.add(message.from_user.id)
                surveys_holder.pop(index)
