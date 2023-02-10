from aiogram.types import Message
from aiogram.dispatcher.filters import Command

from main import bot, dp


@dp.message_handler(Command('new'))
async def start(message: Message):
    await bot.send_message(message.chat.id, 'Вот новые хабы')
