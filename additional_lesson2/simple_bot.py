# Простой телеграм-бот, отправляющий пользователю сообщение.
# Библиотека python-telegram-bot - 20 версия.
from telegram import Bot
# Т.к. библиотека использует асинхронность, нам понадобится
# встроенная библиотека для работы с асинхронностью.
import asyncio


# Токен вы получаете при регистрации бота в спец. боте @BotFather.
TOKEN = '<ваш токен>'
# id пользователя можете узнать у @userinfobot или @getmyid_bot.
USER_ID = 512121057


# Все функции в программе должны предваряться ключевым словом async
# А все вызываемые методы - ключевым словом await
async def main():
    # Создаем экземпляр бота
    bot = Bot(token=TOKEN)

    # Отправка сообщения асинхронным методом send_message()
    # message = 'Салам алейкум!'
    # await bot.send_message(USER_ID, message)

    # Отправка изображения
    photo_ref = 'https://avatars.mds.yandex.net/i?id=e9b61bd7534058ce2d6e3f22a8e90c037d16025e-4377564-images-thumbs&n=13'
    await bot.send_photo(USER_ID, photo_ref)

# Запуск асинхронной функции
asyncio.run(main())
