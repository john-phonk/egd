from loader import bot, dp

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from states.states import States
from middlewares.throttling import rate_limit
from keyboards.inline.dates_keyboard_generation import date_keyboard_generation
from keyboards.inline.main_keyboard import main_keyboard
from keyboards.inline.non_main_keyboards import cancel_keyboard, back_keyboard

from egd_funcs.funcs import get_lessons, get_homework
from mesh.get_answers import get_answers


@dp.message_handler(Command("start"))
@rate_limit(1, 'start')
async def start(message: Message, state: FSMContext):
    await bot.send_message(message.chat.id, '<b>Главное меню</b>', reply_markup=main_keyboard())
    await state.set_state(States.main_menu)

@dp.message_handler(Command("lessons"))
@rate_limit(2, 'lessons')
async def lessons(message: Message, state: FSMContext):
    await bot.send_message(message.chat.id, '<b>Выберите дату:</b>', reply_markup=date_keyboard_generation(type='schedule'))
    await state.set_state(States.get_schedule)

@dp.callback_query_handler(state=States.main_menu)
async def main_menu(query: CallbackQuery, state: FSMContext):
    answer_data = query.data
    if answer_data == 'schedule':
        await query.message.edit_text('<i>Расписание</i>\n<b>Выберите дату:</b>', reply_markup=date_keyboard_generation(type='schedule'))
        await state.set_state(States.get_schedule)

    elif answer_data == 'profile':
        await query.message.edit_text(f'<b>🆔ID:</b> <code>{query["from"]["id"]}</code>\n<b>👤Имя:</b> <code>{query["from"]["first_name"]}</code>', reply_markup=back_keyboard())
        await state.set_state(States.profile)

    elif answer_data == 'homework':
        await query.message.edit_text('<i>Домашняя работа</i>\n<b>Выберите дату:</b>', reply_markup=date_keyboard_generation(type='homework'))
        await state.set_state(States.get_homework)

    elif answer_data == 'answers':
        await query.message.edit_text('<b>Отправь мне ссылку на тест</b>', reply_markup=cancel_keyboard())
        await state.set_state(States.egd_answers)

@dp.callback_query_handler(state=States.get_schedule)
@rate_limit(2, 'get_schedule')
async def get_schedule(query: CallbackQuery, state: FSMContext):
    answer_data = query.data
    if 'get_schedule' in answer_data:
        await query.message.edit_text('<code>Loading...</code>', reply_markup=date_keyboard_generation(type='schedule'))
        answer_data = answer_data.split('.')
        date = [2021, int(answer_data[1]), int(answer_data[0].split(':')[1])]
        lessons = get_lessons(date)
        await query.message.edit_text(lessons, reply_markup=date_keyboard_generation(type='schedule'))

    elif answer_data == 'back':
        await query.message.edit_text('<b>Главное меню</b>', reply_markup=main_keyboard())
        await state.set_state(States.main_menu)

@dp.callback_query_handler(state=States.get_homework)
@rate_limit(2, 'get_homework')
async def get_schedule(query: CallbackQuery, state: FSMContext):
    answer_data = query.data
    if 'get_homework' in answer_data:
        await query.message.edit_text('<code>Loading...</code>', reply_markup=date_keyboard_generation(type='homework'))
        answer_data = answer_data.split('.')
        date = [2021, int(answer_data[1]), int(answer_data[0].split(':')[1])]
        lessons = get_homework(date)
        await query.message.edit_text(lessons, reply_markup=date_keyboard_generation(type='homework'))
        
    elif answer_data == 'back':
        await query.message.edit_text('<b>Главное меню</b>', reply_markup=main_keyboard())
        await state.set_state(States.main_menu)

@dp.message_handler(state=States.egd_answers)
async def send_answer(message: Message, state: FSMContext):
    answer = message.text
    answers = f'{get_answers(link=answer)}<i>Powered by @mdzzz_bot</i>'
    if len(answers) > 4096:
        for x in range(0, len(answers), 4096):
            await bot.send_message(message.chat.id, answers[x:x+4096])
    else:
        await bot.send_message(message.chat.id, answers)
    await bot.send_message(message.chat.id, '<b>Главное меню</b>', reply_markup=main_keyboard())
    await state.set_state(States.main_menu)

@dp.callback_query_handler(state=States.egd_answers)
async def answer(query: CallbackQuery, state: FSMContext):
    answer = query.data
    await query.message.edit_text('<b>Главное меню</b>', reply_markup=main_keyboard())
    await state.set_state(States.main_menu)

@dp.callback_query_handler(state=States.profile)
async def get_schedule(query: CallbackQuery, state: FSMContext):
    answer_data = query.data
    if answer_data == 'back':
        await query.message.edit_text('<b>Главное меню</b>', reply_markup=main_keyboard())
        await state.set_state(States.main_menu)