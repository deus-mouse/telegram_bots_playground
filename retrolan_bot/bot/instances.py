import logging

from aiogram import Bot, Dispatcher, executor, types
from config import ed_bot_token
from types import SimpleNamespace
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton

API_TOKEN = ed_bot_token

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True  # чтобы сворачивалась
                         )

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='форма', url='https://forms.gle/dYLcPHocXMExP15X8')

# ikb.add(ib1, ib2)  # в одной строке
ikb.add(ib1)

text_storage = SimpleNamespace(
    help='<b>/start</b> - <em>начать работу с ботом</em>\n'
         '<b>/help</b> - <em>список команд</em>\n'
         '<b>/link</b> - <em>ссылки</em>\n'
    ,
    start='Привет ! Я инвайт-бот ретро лан, вам необходимо ответить на вопросы общего характера, чтобы мы смогли '
          'немного лучше узнать Вас. Рассмотрение вашей кандидатуры займёт несколько дней, после чего вас пригласят в '
          'чат сбора в гараж.',
)

for button in text_storage.__dict__.keys():
    if button in ['start']:
        continue
    kb.add(KeyboardButton(f'/{button}'))
