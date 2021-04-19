from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from datetime import timedelta, datetime


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def get_dates_range():
    dates = []
    now = datetime.now()
    days = timedelta(12)
    start_date = now - days         
    days = timedelta(13)
    end_date = now + days
    for single_date in daterange(start_date, end_date):
        dates.append(single_date.strftime("%d.%m"))
    return dates

def date_keyboard_generation(type):
    dates = get_dates_range()
    buttons = []
    for btn in dates:
        buttons.append(InlineKeyboardButton(text=f"{btn}", callback_data=f"get_{type}:{btn}"),)
    keyboard = InlineKeyboardMarkup(row_width=5)
    keyboard.add(*buttons)
    keyboard.add(InlineKeyboardButton('Назад', callback_data='back'))
    return keyboard