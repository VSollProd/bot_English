from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import parseLevel
import parseAct
import datetime
import asyncio
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler


BOT_TOKEN = '6168553378:AAF1rIIsRonI2pWwf4orMX0qh4sBDMvY-Xc'
import time

counter_act = 0
kiev = pytz.timezone('Europe/Kiev')
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
parserLvl = parseLevel.WordsParser()

count_stop = 0
now = datetime.datetime.now()



bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
scheduler = AsyncIOScheduler(timezone=kiev)



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
    KeyboardButton('/Обрати за сферою діяльності')
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


    if level == 'A1':
        scheduler.add_job(a1, args=(message,), trigger='cron', hour = 12 , minute = 0)

    elif level == 'A2':
        scheduler.add_job(a2,args=(message,), trigger='cron', hour = 12 , minute = 0)

    elif level == 'B1':
        scheduler.add_job(b1,args=(message,), trigger='cron', hour = 12 , minute = 0)

    elif level == 'B2':
        scheduler.add_job(b2,args=(message,), trigger='cron', hour = 12 , minute = 0)

    elif level == 'C1/2':
        scheduler.add_job(c1,args=(message,), trigger='cron', hour = 12 , minute = 0)


    await bot.send_message(message.from_user.id,
                           f"Ви обрали рівень {level}, тепер вам буде приходить кожен день по 5 слів рівня{level}",
                           reply_markup=CHANGE_KEYBOARD)


@dp.message_handler(commands='Сфера')
async def act_handler(message: types.Message):
    act = message.text.split(' ')[1]  # Получаем сферу из текста сообщения
    global counter_act

    # sfera(message, act)
    await bot.send_message(message.from_user.id,
                               f"Ви обрали сферу {act}, тепер вам буде приходить кожен день по 5 слів зі сфери {act}",
                               reply_markup=CHANGE_KEYBOARD)
    scheduler.add_job(sfera_chng,args=(message, act), trigger='cron', hour=12, minute=0)




def sfera(act):
    global count_stop

    list = []
    if act == 'ІТ':
        obj = parseAct.ParseAct()
        list = obj.parse_IT()
    if act == 'медицини':
        obj = parseAct.ParseAct()
        list = obj.parse_med()
    if act == 'економіки':
        obj = parseAct.ParseAct()
        list = obj.parse_economic()
    if act == 'політики':
        obj = parseAct.ParseAct()
        list = obj.parse_politice()
    if act == 'мистецтво':
        obj = parseAct.ParseAct()
        list = obj.parse_art()
    return list


async def sfera_chng(message : types.Message, act):
    global counter1
    list = sfera(act)
    print('ds')
    await bot.send_message(message.from_user.id, list[counter1])
    await bot.send_message(message.from_user.id, list[counter1 + 1])
    await bot.send_message(message.from_user.id, list[counter1 + 2])
    await bot.send_message(message.from_user.id, list[counter1 + 3])
    await bot.send_message(message.from_user.id, list[counter1 + 4])
    await asyncio.sleep(60)
    counter1 += 5



async def a1(message: types.Message):
    global count_stop
    global counter1
    list = parserLvl.parse_words('A1')
    await bot.send_message(message.from_user.id, list[counter1])
    await bot.send_message(message.from_user.id, list[counter1 + 1])
    await bot.send_message(message.from_user.id, list[counter1 + 2])
    await bot.send_message(message.from_user.id, list[counter1 + 3])
    await bot.send_message(message.from_user.id, list[counter1 + 4])
    await asyncio.sleep(60)

    counter1 += 5



async def a2(message: types.Message):
    global count_stop
    global counter2
    list = parserLvl.parse_words('A2')
    await bot.send_message(message.from_user.id, list[counter1])
    await bot.send_message(message.from_user.id, list[counter1 + 1])
    await bot.send_message(message.from_user.id, list[counter1 + 2])
    await bot.send_message(message.from_user.id, list[counter1 + 3])
    await bot.send_message(message.from_user.id, list[counter1 + 4])
    await asyncio.sleep(60)


async def b1(message: types.Message):
    global count_stop
    global counter1
    list = parserLvl.parse_words('B1')
    await bot.send_message(message.from_user.id, list[counter1])
    await bot.send_message(message.from_user.id, list[counter1 + 1])
    await bot.send_message(message.from_user.id, list[counter1 + 2])
    await bot.send_message(message.from_user.id, list[counter1 + 3])
    await bot.send_message(message.from_user.id, list[counter1 + 4])
    await asyncio.sleep(60)


async def b2(message: types.Message):

    global count_stop
    global counter4
    list = parserLvl.parse_words('B2')
    await bot.send_message(message.from_user.id, list[counter1])
    await bot.send_message(message.from_user.id, list[counter1 + 1])
    await bot.send_message(message.from_user.id, list[counter1 + 2])
    await bot.send_message(message.from_user.id, list[counter1 + 3])
    await bot.send_message(message.from_user.id, list[counter1 + 4])
    await asyncio.sleep(60)


async def c1(message: types.Message):
    global count_stop
    global counter5
    list = parserLvl.parse_words('C1')
    await bot.send_message(message.from_user.id, list[counter1])
    await bot.send_message(message.from_user.id, list[counter1 + 1])
    await bot.send_message(message.from_user.id, list[counter1 + 2])
    await bot.send_message(message.from_user.id, list[counter1 + 3])
    await bot.send_message(message.from_user.id, list[counter1 + 4])
    await asyncio.sleep(60)


scheduler.start()
executor.start_polling(dp, skip_updates=True)
