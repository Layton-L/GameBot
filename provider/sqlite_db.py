from time import time
import sqlite3 as sqlite
from pathlib import Path

from config import DATABASE_NAME, SQLS_FOLDER


def sqlite_start() -> None:
    global db, cursor
    db = sqlite.connect(DATABASE_NAME)
    cursor = db.cursor()

    query = Path(SQLS_FOLDER + "table.sql").read_text()
    cursor.execute(query)
    db.commit()


def user_add(user_id: int) -> None:
    sqlite_start()

    query = "INSERT INTO users (telegram_id, time, bonus_time) VALUES (?, ?, ?)"
    cursor.execute(query, [user_id, int(time()), int(time())])
    db.commit()


def user_delete(user_id: int) -> None:
    sqlite_start()

    query = "DELETE FROM users WHERE telegram_id = ?"
    cursor.execute(query, (user_id,))
    db.commit()


def user_exists(user_id: int) -> bool:
    sqlite_start()
    query = "SELECT * FROM users WHERE telegram_id = ?"

    result = cursor.execute(query, (user_id,)).fetchall()
    db.commit()
    return bool(len(result))


def get_user_info(user_id: int) -> list:
    sqlite_start()
    query = "SELECT * FROM users WHERE telegram_id = ?"

    result = cursor.execute(query, (user_id,)).fetchall()
    db.commit()

    return result[0]


def get_balance(user_id: int) -> int:
    return int(str(get_user_info(user_id)[2]))


def get_bank_balance(user_id: int) -> int:
    return int(str(get_user_info(user_id)[3]))


def get_level(user_id: int) -> int:
    return int(str(get_user_info(user_id)[4]))


def get_exp(user_id: int) -> int:
    return int(str(get_user_info(user_id)[5]))


def get_time(user_id: int) -> int:
    return int(str(get_user_info(user_id)[6]))


def get_bonus_time(user_id: int) -> int:
    return int(str(get_user_info(user_id)[7]))


def set_balance(user_id: int, value: int) -> None:
    sqlite_start()

    query = "UPDATE users SET balance = ? WHERE telegram_id = ?"
    cursor.execute(query, [value, user_id])
    db.commit()


def set_bank_balance(user_id: int, value: int) -> None:
    sqlite_start()

    query = "UPDATE users SET bank_balance = ? WHERE telegram_id = ?"
    cursor.execute(query, [value, user_id])
    db.commit()


def set_level(user_id: int, value: int) -> None:
    sqlite_start()

    query = "UPDATE users SET level = ? WHERE telegram_id = ?"
    cursor.execute(query, [value, user_id])
    db.commit()


def set_exp(user_id: int, value: int) -> None:
    sqlite_start()

    query = "UPDATE users SET exp = ? WHERE telegram_id = ?"
    cursor.execute(query, [value, user_id])
    db.commit()


def set_bonus_time(user_id: int, value: int) -> None:
    sqlite_start()

    query = "UPDATE users SET bonus_time = ? WHERE telegram_id = ?"
    cursor.execute(query, [value, user_id])
    db.commit()


def add_balance(user_id: int, value: int) -> None:
    set_balance(user_id, get_balance(user_id) + value)


def add_bank_balance(user_id: int, value: int) -> None:
    set_bank_balance(user_id, get_bank_balance(user_id) + value)


def add_level(user_id: int, value: int) -> None:
    set_level(user_id, get_level(user_id) + value)


def add_exp(user_id: int, value: int) -> None:
    set_exp(user_id, get_exp(user_id) + value)


def reduce_balance(user_id: int, value: int) -> None:
    set_balance(user_id, get_balance(user_id) - value)


def reduce_bank_balance(user_id: int, value: int) -> None:
    set_bank_balance(user_id, get_bank_balance(user_id) - value)


def reduce_level(user_id: int, value: int) -> None:
    set_level(user_id, get_level(user_id) - value)


def reduce_exp(user_id: int, value: int) -> None:
    set_exp(user_id, get_exp(user_id) - value)