from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb_builder = ReplyKeyboardBuilder()

faculties = [
             "Институт информатики и кибернетики",
             "Авиационный техникум",
             "Биологический факультет",
             "Естественнонаучный институт",
             "Институт авиационной и ракетно-космической техники",
             "Институт двигателей и энергетических установок",
             "Институт дополнительного образования",
             "Институт экономики и управления",
             "Исторический факультет",
             "Механико-математический факультет",
             "Передовая инженерная аэрокосмическая школа",
             "Психологический факультет",
             "Социологический факультет",
             "Факультет филологии и журналистики",
             "Физический факультет",
             "Химический факультет",
             "Юридический институт"
             ]

buttons: list[KeyboardButton] = [KeyboardButton(text=i) for i in faculties]

kb_builder.row(*buttons, width=1)

faculty_reply_markup = kb_builder.as_markup(resize_keyboard=True)
faculty_reply_markup