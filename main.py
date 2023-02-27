from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import parseLevel
import parseAct
import datetime


BOT_TOKEN = '5813656566:AAFXayBd7gVLvn5cAQgvJpUlwbg11r82HPg'
import time

counter_act = 0

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
parserLvl = parseLevel.WordsParser()

now = datetime.datetime.now()

tim = f'{now.hour}:{now.minute}'

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

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


@dp.message_handler(commands='level')
async def level_handler(message: types.Message):
    level = message.text.split(' ')[1]  # Получаем уровень из текста сообщения
    await bot.send_message(message.from_user.id, f"Ви обрали рівень {level}, тепер вам буде приходить кожен день по 5 слів рівня{level}", reply_markup=CHANGE_KEYBOARD)

    
    if level == 'A1':
        await a1(message)
    elif level == 'A2':
        await a2(message)
    elif level == 'B1':
        await b1(message)
    elif level == 'B2':
        await b2(message)
    elif level == 'C1/2':
        await c1(message)


@dp.message_handler(commands='Сфера')
async def act_handler(message: types.Message):
    act = message.text.split(' ')[1]  # Получаем сферу из текста сообщения
    global counter_act
    await bot.send_message(message.from_user.id, f"Ви обрали сферу {act}, тепер вам буде приходить кожен день по 5 слів зі сфери {act}", reply_markup=CHANGE_KEYBOARD)
   

    while True:
        now = datetime.datetime.now()
        tim = now.strftime('%H:%M')

        list = []
        if tim == '23:00':

            if act == 'медицини':
                obj1 = parseAct.ParseAct()
                list = obj1.parse_med()
            if act == 'ІТ':
                obj1 = parseAct.ParseAct()
                list = obj1.parse_IT()
            if act == 'економіки':
                obj1 = parseAct.ParseAct()
                list = obj1.parse_economic()
            if act == 'політики':
                obj1 = parseAct.ParseAct()
                list = obj1.parse_politice()
            if act == 'мистецтво':
                obj1 = parseAct.ParseAct()
                list = obj1.parse_art()

            await bot.send_message(message.from_user.id, list[counter_act])
            await bot.send_message(message.from_user.id, list[counter_act + 1])
            await bot.send_message(message.from_user.id, list[counter_act + 2])
            await bot.send_message(message.from_user.id, list[counter_act + 3])
            await bot.send_message(message.from_user.id, list[counter_act + 4])
            time.sleep(60)
            counter_act += 5
        if message.text == '/Змінити рівень або сферу діяльності':
            break





async def a1(message: types.Message):
    global counter1
    list = parserLvl.parse_words('A1')
    while True:
        now = datetime.datetime.now()
        tim = now.strftime('%H:%M')
        if tim == '12:00':
            await bot.send_message(message.from_user.id, list[counter1])
            await bot.send_message(message.from_user.id, list[counter1 + 1])
            await bot.send_message(message.from_user.id, list[counter1 + 2])
            await bot.send_message(message.from_user.id, list[counter1 + 3])
            await bot.send_message(message.from_user.id, list[counter1 + 4])
            time.sleep(60)
            counter1 += 5
        if message.text == '/Змінити рівень або сферу діяльності':
            break


async def a2(message: types.Message):
    global counter2
    list = parserLvl.parse_words('A2')
    while True:
        now = datetime.datetime.now()
        tim = now.strftime('%H:%M')
        if tim == '12:00':
            await bot.send_message(message.from_user.id, list[counter2])
            await bot.send_message(message.from_user.id, list[counter2 + 1])
            await bot.send_message(message.from_user.id, list[counter2 + 2])
            await bot.send_message(message.from_user.id, list[counter2 + 3])
            await bot.send_message(message.from_user.id, list[counter2 + 4])
            time.sleep(60)
            counter2 += 5
        if message.text == '/Змінити рівень або сферу діяльності':
            break


async def b1(message: types.Message):
    global counter1
    list = parserLvl.parse_words('B1')
    while True:
        now = datetime.datetime.now()
        tim = now.strftime('%H:%M')
        if tim == '12:00':
            await bot.send_message(message.from_user.id, list[counter3])
            await bot.send_message(message.from_user.id, list[counter3 + 1])
            await bot.send_message(message.from_user.id, list[counter3 + 2])
            await bot.send_message(message.from_user.id, list[counter3 + 3])
            await bot.send_message(message.from_user.id, list[counter3 + 4])
            time.sleep(60)
            counter1 += 5
        if message.text == '/Змінити рівень або сферу діяльності':
            break


async def b2(message: types.Message):
    global counter4
    list = parserLvl.parse_words('B2')
    while True:
        now = datetime.datetime.now()
        tim = now.strftime('%H:%M')
        if tim == '12:00':
            await bot.send_message(message.from_user.id, list[counter4])
            await bot.send_message(message.from_user.id, list[counter4 + 1])
            await bot.send_message(message.from_user.id, list[counter4 + 2])
            await bot.send_message(message.from_user.id, list[counter4 + 3])
            await bot.send_message(message.from_user.id, list[counter4 + 4])
            time.sleep(60)
            counter4 += 5
        if message.text == '/Змінити рівень або сферу діяльності':
            break


async def c1(message: types.Message):
    global counter5
    list = parserLvl.parse_words('C1')
    while True:
        now = datetime.datetime.now()
        tim = now.strftime('%H:%M')
        if tim == '12:00':
            await bot.send_message(message.from_user.id, list[counter5])
            await bot.send_message(message.from_user.id, list[counter5 + 1])
            await bot.send_message(message.from_user.id, list[counter5 + 2])
            await bot.send_message(message.from_user.id, list[counter5 + 3])
            await bot.send_message(message.from_user.id, list[counter5 + 4])
            time.sleep(60)
            counter5 += 5
        if message.text == '/Змінити рівень або сферу діяльності':
            break


executor.start_polling(dp, skip_updates=True)
