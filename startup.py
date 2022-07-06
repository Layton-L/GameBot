from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from config import TELEGRAM_TOKEN

storage = RedisStorage2(db=5, pool_size=10, prefix="my_fsm_key")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)