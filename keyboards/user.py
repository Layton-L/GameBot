from aiogram.types import ReplyKeyboardMarkup

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add("Статистика", "Настройки")
main_menu.add("Игры", "Банк", "Бонус")

settings_menu = ReplyKeyboardMarkup(resize_keyboard=True)
settings_menu.add("Перевести деньги")
settings_menu.add("Назад")

games_menu = ReplyKeyboardMarkup(resize_keyboard=True)
games_menu.add("Орёл или решка")
games_menu.add("Кубик", "Казино")
games_menu.add("Назад")

bank_menu = ReplyKeyboardMarkup(resize_keyboard=True)
bank_menu.add("Пополнить счёт")
bank_menu.add("Вывести деньги")
bank_menu.add("Баланс", "Назад")