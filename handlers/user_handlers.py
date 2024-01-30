import pandas as pd

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.context import FSMContext

from lexicon.lexicon_ru import LEXICON_RU
from utils.parse import parse_data

class FSMdata(StatesGroup):
    fill_faculty = State()
    fill_group = State()


database = pd.read_csv("database.csv", names=["faculty", "group"], index_col=0)

router = Router()

@router.message(Command(commands='start'))
async def process_start_help_command(message: Message, state: FSMContext):
    await message.reply(LEXICON_RU["/start"])
    await message.reply(LEXICON_RU["/set_faculty"])
    await state.set_state(FSMdata.fill_faculty)

@router.message(Command(commands='today'), StateFilter(default_state))
async def process_timetable_command(message: Message):
    user_id = message.from_user.id
    if user_id in database.index:
        subj_lst = parse_data(database.at[user_id, "faculty"], database.at[user_id, "group"])
        is_void = lambda x: x if x else "Сегодня нет пар!"
        await message.reply(is_void(subj_lst))
    else:
        await message.reply("Сначала заполните данные!")

@router.message(Command(commands='set_faculty'), StateFilter(default_state))
async def process_faculty_command(message: Message, state: FSMContext):
    await state.set_state(FSMdata.fill_faculty)
    await message.reply(LEXICON_RU["/set_faculty"])

@router.message(StateFilter(FSMdata.fill_faculty))
async def process_faculty_command(message: Message, state: FSMContext):
    await state.set_state(FSMdata.fill_group)
    await state.update_data(faculty=message.text)
    await message.reply(LEXICON_RU["/set_group"])
    

@router.message(StateFilter(FSMdata.fill_group))
async def process_group_command(message: Message, state: FSMContext):
    await state.update_data(group=message.text)
    data = await state.get_data()
    database.loc[message.from_user.id] = [data["faculty"], data["group"]]
    database.to_csv("database.csv", index=True, header=False)
    await state.clear()
    await message.reply("Данные заполнены")

@router.message(Command(commands='set_group'), StateFilter(default_state))
async def process_group_command(message: Message, state: FSMContext):
    await message.reply(LEXICON_RU["/set_group"])
    await state.set_state(FSMdata.fill_group)

@router.message()
async def process_no_command(message: Message):
    await message.reply(LEXICON_RU["no_command"])