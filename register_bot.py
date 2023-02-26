from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config_4am_psybot


storage = MemoryStorage()

bot = Bot(token=config_4am_psybot.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot, storage=storage)


