from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def cancel_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    inline_btn_1 = InlineKeyboardButton('Отмена', callback_data='cancel')
    keyboard.add(inline_btn_1)
    return keyboard

def back_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    inline_btn_1 = InlineKeyboardButton('Назад', callback_data='back')
    keyboard.add(inline_btn_1)
    return keyboard