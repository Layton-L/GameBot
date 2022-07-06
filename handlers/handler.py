from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

import random
import tzlocal
from time import time
from datetime import datetime, timedelta

from config import ADMINS_IDS
from provider import sqlite_db
from states.states import States
from keyboards import user as user_kb, admin as admin_kb


async def start(message: types.Message):
    user_id = message.from_user.id
    if not sqlite_db.user_exists(user_id):
        sqlite_db.user_add(user_id)

    await message.answer("Меню:", reply_markup=user_kb.main_menu)


async def admin(message: types.Message):
    if message.from_user.id in ADMINS_IDS:
        await message.answer("Админ меню:", reply_markup=admin_kb.main_menu)
        await States.menu.set()


async def statistics(message: types.Message):
    user_id = message.from_user.id
    await message.answer(f"Имя: {message.from_user.full_name}\n"
                         f"Дата регистрации: {datetime.fromtimestamp(sqlite_db.get_time(user_id), tzlocal.get_localzone()).strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                         f"Баланс: {sqlite_db.get_balance(user_id)}\n"
                         f"Баланс в банке: {sqlite_db.get_bank_balance(user_id)}\n"
                         f"Уровень: {sqlite_db.get_level(user_id)}\n"
                         f"Опыт: {sqlite_db.get_exp(user_id)}")


async def settings(message: types.Message):
    await message.answer("Настройки:", reply_markup=user_kb.settings_menu)
    await States.menu.set()


async def bank(message: types.Message):
    await message.answer("Банк:", reply_markup=user_kb.bank_menu)
    await States.menu.set()


async def games(message: types.Message):
    await message.answer("Игры:", reply_markup=user_kb.games_menu)
    await States.menu.set()


async def bonus(message: types.Message):
    user_id = message.from_user.id
    bonus_time = sqlite_db.get_bonus_time(user_id)
    if bonus_time > time():
        duration = bonus_time - int(time())
        await message.answer(f"Вы уже получили бонус, приходите через: {timedelta(0, duration)}")
        return
    value = random.randint(10, 1000)
    sqlite_db.add_balance(user_id, value)
    sqlite_db.set_bonus_time(user_id, int(time()) + 21600)
    await message.answer(f"Вы получили бонус в размере: {value}")


async def back(message: types.Message, state: FSMContext):
    await message.answer("Меню:", reply_markup=user_kb.main_menu)
    await state.finish()


def register_handler(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start", "старт", "menu", "меню"], state="*")
    dp.register_message_handler(admin, commands=["admin", "админ"], state="*")

    dp.register_message_handler(statistics, Text(equals="статистика", ignore_case=True))
    dp.register_message_handler(settings, Text(equals="настройки", ignore_case=True))
    dp.register_message_handler(bank, Text(equals="банк", ignore_case=True))
    dp.register_message_handler(games, Text(equals="игры", ignore_case=True))
    dp.register_message_handler(bonus, Text(equals="бонус", ignore_case=True))

    dp.register_message_handler(back, Text(equals="назад", ignore_case=True), state=States.menu)
    dp.register_message_handler(settings, Text(equals="отмена", ignore_case=True), state=States.send_money)
    dp.register_message_handler(settings, Text(equals="отмена", ignore_case=True), state=States.send_money_value)
