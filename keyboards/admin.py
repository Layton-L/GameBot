from aiogram.types import ReplyKeyboardMarkup

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add("Управление пользователем")
main_menu.add("Назад")

management_menu = ReplyKeyboardMarkup(resize_keyboard=True)
management_menu.add("Добавить пользователя")
management_menu.add("Удалить пользователя")
management_menu.add("Назад")