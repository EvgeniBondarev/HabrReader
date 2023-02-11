from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

new_posts = KeyboardButton('Новые статьи')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(new_posts)

greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(new_posts)