import logging

from aiogram import Bot, Dispatcher, executor, types
from config import ed_bot_token
from types import SimpleNamespace
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


API_TOKEN = ed_bot_token

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         # one_time_keyboard=True
                         )

text_storage = SimpleNamespace(
    help='<b>/help</b> - <em>список команд</em>\n'
         '<b>/start</b> - <em>начать работу с ботом</em>\n'
         '<b>/description</b> - <em>описание</em>\n'
         '<b>/give</b> - <em>стикер</em>\n'
         '<b>/image</b> - <em>image</em>\n'
         '<b>/location</b> - <em>location</em>\n'
    ,
    start='Привет, я бот',
    description='my description',
    image='image',
)

for button in text_storage.__dict__.keys():
    print(f'{button=}')
    if button in ['start']:
        continue
    kb.add(KeyboardButton(f'/{button}'))
