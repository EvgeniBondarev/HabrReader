from aiogram.types import Message, PreCheckoutQuery
from aiogram.dispatcher.filters import Command

from main import bot, dp, db

from keyboards.web_app import app_keyboard

@dp.message_handler(Command('start'))
async def start(message: Message):
    await bot.send_message(message.chat.id,
                           'Перейдите к выбору хабoв',
                           reply_markup=app_keyboard)
    db.new_user(message.chat.id, "all")

@dp.message_handler(content_types='web_app_data')
async def buy_process(web_app_message):
    db.update_user(web_app_message.chat.id, web_app_message.web_app_data.data)
