import csv
import pandas as pd
from environs import Env

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

import utils

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def process_start_help_command(message: Message):
    await message.reply('Хей, я твое карманное рассписание на сегодня!\nОтправь команду today, чтобы узнать какие сегодня пары')


async def process_timetable_command(message: Message):
    subj_lst = utils.parse.parse_data("Институт информатики и кибернетики", "6212-100503D")
    is_void = lambda x: x if x else "Сегодня нет пар!"
    await message.reply(is_void(subj_lst))

async def process_faculty_command(message: Message):
    await message.reply("Напишите какой у вас факультет")
    pass


async def process_group_command(message: Message):
    pass


async def process_no_command(message: Message):
    await message.reply("Не знаю такой команды...")


# Регистрируем хэндлеры
dp.message.register(process_start_help_command, Command(commands=['start', 'help']))
dp.message.register(process_timetable_command, Command(commands='today'))
dp.message.register(process_faculty_command, Command(commands='faculty'))
dp.message.register(process_group_command, Command(commands='group'))
dp.message.register(process_no_command)

if __name__ == '__main__':
    dp.run_polling(bot)