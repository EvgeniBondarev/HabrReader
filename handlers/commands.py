from aiogram.types import Message, ParseMode
from aiogram.dispatcher.filters import Command

from main import bot, dp, db

from keyboards.web_app import app_keyboard
from habr_pars import pars_posts


@dp.message_handler(Command('start'))
async def start(message: Message):
    await bot.send_message(message.chat.id,
                           'Перейдите к выбору хабoв',
                           reply_markup=app_keyboard)
    db.change_user(message.chat.id, "all")

@dp.message_handler(content_types='web_app_data')
async def buy_process(web_app_message):
    db.change_user(web_app_message.chat.id, web_app_message.web_app_data.data)


@dp.message_handler(Command('new'))
async def start(message: Message):
    await bot.send_message(message.chat.id, db.get_habrs(message.chat.id))
    await send_posts(message.chat.id, pars_posts(db.get_habrs(message.chat.id)))


async def send_posts(chat_id, posts_data):
    for post in posts_data:
        await bot.send_message(chat_id,
                               text=f"<a href='{post['link']}'>{post['rating']}</a>", #сделать переход на сайт по тапу на картинку
                               parse_mode="HTMl")







