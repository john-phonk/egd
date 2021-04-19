import dnevnik
import datetime
from data import config


LOGIN = config.LOGIN
PASSWORD = config.PASSWORD
DRIVER_PATH = config.DRIVER_PATH

def start_session():
    global client
    client = dnevnik.Client(login=LOGIN, password=PASSWORD, use_selenium=True, selenium_executable_path=DRIVER_PATH)

def get_homework(date):
    date_to = datetime.date(date[0], date[1], date[2])
    homework_text = f'<b>Домашняя работа на</b> <code>{date[2]}.{date[1]}.{date[0]}</code>:\n\n'
    date_from = date_to
    try:
        homeworks = client.get_homeworks(begin_prepared_date=date_from, end_prepared_date=date_to)
    except:
        start_session()
        homeworks = client.get_homeworks(begin_prepared_date=date_from, end_prepared_date=date_to)
    for homework in homeworks:
        homework_text += f"<b>{homework['homework_entry']['homework']['subject']['name']} -</b>  <code>{homework['homework_entry']['description']}</code>\n"
    return homework_text

def get_lessons(date):
    date_to = datetime.date(date[0], date[1], date[2])
    lessons_text = f'<b>Расписание на</b> <code>{date[2]}.{date[1]}.{date[0]}</code>:\n\n'
    date_from = date_to
    try:
        lessons = client.get_lessons(date_from=date_from, date_to=date_to)
    except:
        start_session()
        lessons = client.get_lessons(date_from=date_from, date_to=date_to)
    for lesson in lessons:
        lessons_text += f"<code>{lesson.lesson_number}.</code> <b>{lesson.subject_name}</b>\n"
    return lessons_text