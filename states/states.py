from aiogram.dispatcher.filters.state import State, StatesGroup


class States(StatesGroup):
    menu = State()
    admin_menu = State()
    send_money = State()
    send_money_value = State()