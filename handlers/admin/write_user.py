from aiogram import types
from aiogram.dispatcher import FSMContext

from filters import CheckAdmin
from loader import dp, bot
from states.state_users import Message_all_users

from utils.db_api import postgres


@dp.message_handler(CheckAdmin(), text='✍️Написать пользователям')
async def write_user(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ назад')
    await message.answer(text='Введите сообщение пользователям', reply_markup=keyboard)

    await Message_all_users.message_users.set()


@dp.message_handler(text='⬅️ назад', state=Message_all_users.message_users)
async def channel(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('👥 Кол-во пользователей')
    keyboard.row('📱 Найти пользователя')
    keyboard.row('✍️Написать пользователям')
    keyboard.row('⬅️ назад')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Добро пожаловать в меню администратора',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(state=Message_all_users.message_users)
async def answer_admin(message: types.Message, state: FSMContext):
    admin_message = message.text
    users = await postgres.get_all_users()
    for user in users:
        c = user['user_id']
        await bot.send_message(chat_id=c,
                               text=f'Вам написал администратор: {message.from_user.full_name}'
                                    f'\n'
                                    f'Сообщение: {admin_message}')
    await state.finish()
