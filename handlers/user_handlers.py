from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from lexicon.lexicon_ru import LEXICON_RU
from utils.parse import parse_data

router = Router()

@router.message(Command(commands=['help', 'start']))
async def process_start_help_command(message: Message):
    await message.reply(LEXICON_RU["/start, /help"])

@router.message(Command(commands='today'))
async def process_timetable_command(message: Message):
    subj_lst = parse_data("Институт информатики и кибернетики", "6212-100503D")
    is_void = lambda x: x if x else "Сегодня нет пар!"
    await message.reply(is_void(subj_lst))

@router.message(Command(commands='set_faculty'))
async def process_faculty_command(message: Message):
    await message.reply(LEXICON_RU["/set_faculty"])
    pass

@router.message(Command(commands='set_group'))
async def process_group_command(message: Message):
    pass

@router.message()
async def process_no_command(message: Message):
    await message.reply(LEXICON_RU["no_command"])