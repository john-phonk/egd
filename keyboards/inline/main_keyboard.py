from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    inline_btn_1 = InlineKeyboardButton('Профиль', callback_data='profile')
    inline_btn_2 = InlineKeyboardButton('Домашняя работа', callback_data='homework')
    inline_btn_3 = InlineKeyboardButton('Расписание', callback_data='schedule')
    inline_btn_4 = InlineKeyboardButton('МЭШ ответы', callback_data='answers')
    keyboard.add(inline_btn_1, inline_btn_2, inline_btn_3, inline_btn_4)
    return keyboard
