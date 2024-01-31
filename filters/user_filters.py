import re
from aiogram.types import Message

def group_filter(group: Message):
    group = group.text
    pattern = r'\d{4}-\d{6}\w'
    return bool(re.fullmatch(pattern=pattern, string=group))

def faculty_filter(faculty: Message):
    faculty = faculty.text
    words = faculty.split()
    return all(map(lambda x: True if x.isalpha() else False, words))
