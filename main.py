import asyncio
from aiogram import Bot, Dispatcher, executor

from config import TOKENS

loop = asyncio.new_event_loop()
bot = Bot(TOKENS["bot_token"], parse_mode='HTML')
dp = Dispatcher(bot, loop)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp)
