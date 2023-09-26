# Приложение телеграм-бота, реагирующего на сообщения пользователя
from telegram.ext import Application, MessageHandler, CommandHandler, filters
from telegram import KeyboardButton, ReplyKeyboardMarkup


TOKEN = '<ваш токен>'


# Создаем объект приложения через builder()
app = Application.builder().token(TOKEN).build()


# Функция обработки команды /start .
# Все подобные функции принимают аргументы update и context,
# хранящие информацию о текущем боте, пользователе, чате и сообщениях.
async def start(update, context):
    # Получаем id текущего чата через словарь update
    chat_id = update.effective_chat.id
    username = update.message.from_user.first_name
    # Отравляем сообщения через бота, объект которого берем из объекта context
    await context.bot.send_message(chat_id=chat_id, text=f'Салам, {username}!')


# Функция обработки обычных сообщений
async def echo_answer(update, context):
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text=update.message.text)


# Функция обработки команды show_buttons, показывающей пользователю кнопки
async def show_buttons(update, context):
    # Создадим список списков с кнопками
    keyboard = [
        [
            KeyboardButton('Кнопка 1'),
            KeyboardButton('Кнопка 2')
        ],
        [
            KeyboardButton('Кнопка 3'),
            KeyboardButton('Кнопка 4'),
            KeyboardButton('Кнопка 5'),
        ],
        [
            KeyboardButton('Кнопка 6'),
            KeyboardButton('Кнопка 7')
        ],
    ]
    # На основе списка сгенерируем объект разметки клавиатуры
    reply_markup = ReplyKeyboardMarkup(keyboard)
    # Ответим на сообщение пользователя данной структурой
    await update.message.reply_text(
        'Выберите вариант: ', reply_markup=reply_markup)


# Обработчик команд
app.add_handler(CommandHandler('start', start))
# Обработчик сообщений с использованием фильтров
# https://docs.python-telegram-bot.org/en/v20.5/telegram.ext.filters.html
# Операции над фильтрами: AND - &, OR - |, NOT - ~
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_answer))
# Обработчик команды для вызова кнопок
app.add_handler(CommandHandler('show_buttons', show_buttons))

# Запускаем обработку сообщений
app.run_polling()
