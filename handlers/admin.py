from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from keyboards import admin as admin_kb
from states.states import States


async def management(message: types.Message):
    await message.answer("Управление пользователем:", reply_markup=admin_kb.management_menu)
    await States.admin_menu.set()


async def back(message: types.Message):
    await message.answer("Админ меню:", reply_markup=admin_kb.main_menu)
    await States.menu.set()


def register_admin_handler(dp: Dispatcher):
    dp.register_message_handler(management, Text(equals="управление пользователем", ignore_case=True))
    dp.register_message_handler(back, Text(equals="назад", ignore_case=True), state=States.admin_menu)