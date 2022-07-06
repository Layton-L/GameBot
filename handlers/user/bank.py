from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from provider import sqlite_db


async def balance(message: types.Message):
    await message.answer(f"Баланс: {sqlite_db.get_bank_balance(message.from_user.id)}")


def register_bank_handler(dp: Dispatcher):
    dp.register_message_handler(balance, Text(equals="баланс", ignore_case=True), state="*")