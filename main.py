from aiogram import executor

from loader import dp, bot, storage
import handlers
import middlewares
from utils.notify_admin import on_startup_notify
from egd_funcs.funcs import start_session


async def on_startup(dispatcher):
    start_session()
    await on_startup_notify(dispatcher)
    middlewares.setup(dp)

async def on_shutdown(dp):
    await bot.close()
    await storage.close()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown,  skip_updates=True)


