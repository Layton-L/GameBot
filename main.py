from aiogram.utils import executor

from startup import dp
from provider import sqlite_db
from handlers.handler import register_handler
from handlers.admin import register_admin_handler
from handlers.user.bank import register_bank_handler
from handlers.user.settings import register_settings_handler


async def on_startup(_):
    print("Бот запущен")


async def on_shutdown(_):
    print("Бот выключен")


register_handler(dp)
register_admin_handler(dp)
register_bank_handler(dp)
register_settings_handler(dp)

sqlite_db.sqlite_start()
executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)