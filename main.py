import asyncio
from aiogram import Bot, Dispatcher, executor

from config import TOKENS
from db.habrs_data import Database


loop = asyncio.new_event_loop()
bot = Bot(TOKENS["bot_token"], parse_mode='HTML')
dp = Dispatcher(bot, loop)
db = Database("db/useres.db")

if __name__ == '__main__':
    from handlers.commands import dp
    executor.start_polling(dp)
