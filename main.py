from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import parseLevel
import parseAct
import datetime
import random
import asyncio
import pytz
import sqlite3
from apscheduler.schedulers.asyncio import AsyncIOScheduler

BOT_TOKEN = '6168553378:AAF1rIIsRonI2pWwf4orMX0qh4sBDMvY-Xc'

conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, category TEXT)''')

conn1 = sqlite3.connect('users2.db')
cursor1 = conn.cursor()
cursor1.execute('''CREATE TABLE IF NOT EXISTS users2 (user_id INTEGER PRIMARY KEY, category TEXT)''')

kiev = pytz.timezone('Europe/Kiev')

parserLvl = parseLevel.WordsParser()

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

ids = []
acts = []

CHANGE_KEYBOARD = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("/Змінити рівень або сферу діяльності")
)

LEVEL_KEYBOARD = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton('/level A1'),
    KeyboardButton('/level A2'),
    KeyboardButton('/level B1'),
    KeyboardButton('/level B2'),
    KeyboardButton('/level C1/2'),
)

ACTIVITY_KEYBOARD = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton('/Сфера медицини'),
    KeyboardButton('/Сфера ІТ'),
    KeyboardButton('/Сфера економіки'),
    KeyboardButton('/Сфера політики'),
    KeyboardButton('/Сфера мистецтво')
)

MAIN_KEYBOARD = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('/0брати за рівнем'),
    # KeyboardButton('/Обрати за сферою діяльності')
)


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Привіт, це бот для вивчення аглійських слів, тут можно обрати свою сферу або свій рівень англійскої мови(А1,В2.....). Обери нижче! \n Після того як оберете тип слів що вам треба вивчати вам буде приходити 5 слів кожний день о 12:00 день.",
                           reply_markup=MAIN_KEYBOARD)


@dp.message_handler(commands='0брати')
async def choose_level_handler(message: types.Message):
    await bot.send_message(message.from_user.id, "Оберіть рівень.", reply_markup=LEVEL_KEYBOARD)


@dp.message_handler(commands='Обрати')
async def choose_activity_handler(message: types.Message):
    await bot.send_message(message.from_user.id, "Оберіть свою сферу", reply_markup=ACTIVITY_KEYBOARD)


@dp.message_handler(commands='Змінити')
async def stop(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Привіт, це бот для вивчення аглійських слів, тут можно обрати свою сферу або свій рівень англійскої мови(А1,В2.....). Обери нижче! \n Після того як оберете тип слів що вам треба вивчати вам буде приходити 5 слів кожний день о 12:00 день.",
                           reply_markup=MAIN_KEYBOARD)


@dp.message_handler(commands='level')
async def level_handler(message: types.Message):
    level = message.text.split(' ')[1]  # Получаем уровень из текста сообщения
    prs = parseLevel.WordsParser()
    list = prs.parse_words(level)
    smpl = random.sample(list, 5)
    for i in smpl:
        await bot.send_message(message.from_user.id, i)
    # await bot.send_message(message.from_user.id,
    #                         ''
    #                        ,
    #                        reply_markup=CHANGE_KEYBOARD)


# @dp.message_handler(commands='Сфера')
# async def act_handler(message: types.Message):
#     act = message.text.split(' ')[1]  # Получаем сферу из текста сообщения
#
#     list = parseAct.parse_words(act)
#     await bot.send_message(message.from_user.id,
#                            list,
#                            reply_markup=CHANGE_KEYBOARD)


# async def send_words():
#     cursor.execute("SELECT user_id FROM users")
#     for i in cursor.fetchall():
#         ids.append(i[0])

#     cursor.execute("SELECT category FROM users")
#     for i in cursor.fetchall():
#         acts.append(i[0])

#     for k in range(0, len(ids)):
#         print(k)
#         global counter5

#         sample = random.sample(list, 5)
#         for i in sample:
#             await bot.send_message(ids[k], i)


# async def sfera_chng():
#     cursor1.execute("SELECT user_id FROM users2")
#     for i in cursor1.fetchall():
#         ids.append(i[0])

#     cursor1.execute("SELECT category FROM users2")
#     for i in cursor1.fetchall():
#         acts.append(i[0])

#     for k in range(0, len(ids)):
#         global counter5
#         list = parserLvl.parse_words(acts[k])
#         sample1 = random.sample(list, 5)
#         for i in sample1:
#             await bot.send_message(ids[k], i)


executor.start_polling(dp)
