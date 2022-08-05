from aiogram import types

from data.prolong_sub import prolong_sub
from filters import CheckUsers, CheckAdmin
from loader import dp, bot

@dp.message_handler(CheckAdmin(), text='⬅️ назад')
async def my_profile(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом', '👨‍💻 Админ')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы вернулись в главное меню',
                           reply_markup=keyboard)

@dp.message_handler(CheckUsers(), text='⬅️ назад')
async def my_profile(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы вернулись в главное меню',
                           reply_markup=keyboard)
