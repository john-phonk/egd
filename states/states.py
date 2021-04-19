from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    main_menu = State()
    egd_answers = State()
    get_homework = State()
    get_schedule = State()
    profile = State()