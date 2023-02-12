from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command
import aiogram.utils.markdown as fmt

from main import bot, dp, db

from keyboards.web_app import app_keyboard
from keyboards.new_posts import greet_kb1
from habr_pars import pars_posts


@dp.message_handler(Command('start'))
async def start(message: Message):
    await bot.send_message(message.chat.id,
                           'Перейдите к выбору хабoв',
                           reply_markup=app_keyboard)


@dp.message_handler(content_types='web_app_data')
async def buy_process(web_app_message):
    db.change_user(web_app_message.chat.id, web_app_message.web_app_data.data)
    await bot.send_message(web_app_message.chat.id, "Новые посты", reply_markup=greet_kb1)


@dp.message_handler(Command('new'))
@dp.message_handler(text='Новые статьи')
async def start(message: Message):
    await bot.send_message(message.chat.id, "Несколько новых статей", reply_markup=ReplyKeyboardRemove())
    await send_posts(message.chat.id, pars_posts(db.get_habrs(message.chat.id)))


async def send_posts(chat_id, posts_data):
    for post in posts_data:
        await bot.send_message(chat_id,
                               text=f"<a href='{post['link']}'>{fmt.hide_link(post['link'])}{post['rating']}\n{post['reading_time']}\n{post['type']}</a>",
                               parse_mode="HTML")

    await bot.send_message(chat_id, "Ваши хабры:", reply_markup=greet_kb1)









