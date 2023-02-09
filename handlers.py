from aiogram.types import Message, PreCheckoutQuery
from aiogram.dispatcher.filters import Command

from main import bot, dp

from keyboards import keyboard

@dp.message_handler(Command('start'))
async def start(message: Message):
    await bot.send_message(message.chat.id,
                           'Тестируем WebApp',
                           reply_markup=keyboard)

@dp.message_handler(Command('id'))
async def start(message: Message):
    await bot.send_message(message.chat.id, message.chat.id)


@dp.message_handler(content_types='web_app_data')
async def buy_process(web_app_message):
    print(web_app_message)
    print(web_app_message.web_app_data.data)

@dp.pre_checkout_query_handler(lambda q: True)
async def checkout_process(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)