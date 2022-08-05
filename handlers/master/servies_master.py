from aiogram import types

from data.prolong_sub import prolong_sub
from filters import CheckMaster
from loader import dp, bot
from utils.db_api import postgres


@dp.message_handler(CheckMaster(), text='💅 Услуги')
async def edit_profile(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
    keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
    keyboard.row('✍️Редактировать свой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите услуги, которые будете предоставлять',
                           reply_markup=keyboard)
