<h1>HabrReader</h1>

<h2>задачи</h2>

<ul>
    <li>Парсинг всех статей + теги статей, дальше по интересам</li>
    <li>Чтение в телеграмовской адаптации сайтов + ссылка в начале на оригинал</li><br><br>
<li>Настройки и предпочтения в закрепе, или просто в комменте (без бд!)<br>
        Ршение:

        import logging

        from aiogram import Bot, Dispatcher, executor, types
        
        API_TOKEN = 'BOT_TOKEN_HERE'
        
        # Configure logging
        logging.basicConfig(level=logging.INFO)
        
        # Initialize bot and dispatcher
        bot = Bot(token=API_TOKEN)
        dp = Dispatcher(bot)
        
        @dp.message_handler(commands='pinned')
        async def cmd_pinned(message: types.Message):
            channel = message.chat
            pinned_message = await channel.get_pinned_message()
            await message.answer(f'Pinned message: {pinned_message}')
        
        if __name__ == '__main__':
            executor.start_polling(dp, skip_updates=True)
</li>
    <li>Повышение рейтинга при переходе по ссылке на пост или тапе смайли в низу, если смайл плохой, то удаляем сообщение и понижаем статус</li>
    <li>Создовать одноразовые ссылки и проверять на активность (если активна, то повышаем репу по тегам поста)</li>
    <li>Начальные настройки берутся из тегов на хобре</li>
    <li>Если тыкнул на пост с python, то появляется поле python в конфиг сиообщении "python ++1"</li>
        <ul>
            <li>И с минусами тоже самое</li>
            <li>Откланил 👎 = минус репа</li>
            <li>Удаление дизлайкнутых постов при добовлении нового поста</li>
        </ul>
</ul>


