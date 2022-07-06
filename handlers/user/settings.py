from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from provider import sqlite_db
from states.states import States
from keyboards import keyboard, user


async def send_money_start(message: types.Message):
    await message.answer("Пожалуйста, введите ID пользователя", reply_markup=keyboard.cancel_menu)
    await States.send_money.set()


async def send_money(message: types.Message, state: FSMContext):
    try:
        user_id = int(message.text)
        if not sqlite_db.user_exists(user_id):
            await message.answer("Пользователь не существует")
            return
        if message.from_user.id == user_id:
            await message.answer("Ты не можешь отправить деньги себе")
            return
        await state.update_data(user_id=user_id)
        await States.send_money_value.set()
        await message.answer("Пожалуйста, введите сумму перевода")
    except:
        await message.answer("ID должен быть числом")


async def send_money_value(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()
        user_id = int(data["user_id"])
        value = int(message.text)
        if value <= 0:
            await message.answer("Сумма должна быть больше 0")
            return
        if sqlite_db.get_balance(message.from_user.id) < value:
            await message.answer("У вас недостаточно денег")
            return
        sqlite_db.reduce_balance(message.from_user.id, value)
        sqlite_db.add_balance(user_id, value)
        await message.answer(f"Ты сделал перевод на сумму: {value}", reply_markup=user_kb.settings_menu)
        await state.finish()
    except:
        await message.answer("Сумма должна быть числом")


def register_settings_handler(dp: Dispatcher):
    dp.register_message_handler(send_money_start, Text(equals="перевести деньги", ignore_case=True), state="*")
    dp.register_message_handler(send_money, state=States.send_money)
    dp.register_message_handler(send_money_value, state=States.send_money_value)