from aiogram import types

from filters import CheckAdmin
from loader import dp
from utils.db_api import postgres


@dp.message_handler(CheckAdmin(), text='👥 Кол-во пользователей')
async def count_users(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('👥 Кол-во пользователей')
    keyboard.row('📱 Найти пользователя')
    keyboard.row('✍️Написать пользователям')
    keyboard.row('⬅️ назад')

    count_users = await postgres.count_users()
    users = await postgres.get_all_info_users()
    master = 0
    client = 0
    for user in users:
        if (user['manicure_pedicure'] and user['hairdresser'] and user['visage'] and user['other_services']) != 'Пусто':
            master += 1

        else:
            client += 1
    await message.answer(text=f"Пользователей: {count_users[0]['count']}\n"
                              f"Мастеров: {master}\n"
                              f"Клиентов: {client}\n", reply_markup=keyboard)
