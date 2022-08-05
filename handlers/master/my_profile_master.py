from aiogram import types

from data.profile import services_master, profile_user
from data.prolong_sub import prolong_sub
from filters import CheckUsers, CheckMaster, CheckClient
from loader import dp, bot
from utils.db_api import postgres


@dp.message_handler(CheckUsers(), text='📂 Мой профиль')
async def my_profile(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('📋 Посмотерть свой профиль')
    keyboard.row('✍️Редактировать свой профиль')
    keyboard.row('⬅️ назад')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Здесь вы можете посмотеть свой профиль или редактировать его',
                           reply_markup=keyboard)


@dp.message_handler(CheckUsers(), text='📋 Посмотерть свой профиль')
async def view_profile(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('✍️Редактировать свой профиль')
    keyboard.row('⬅️ назад')
    user = await postgres.get_user(user_id=message.from_user.id)
    services = await services_master(user_id=message.from_user.id)

    if await postgres.check_rating_master(user_id=message.from_user.id):
        rating = await postgres.select_rating_master(user_id=message.from_user.id)
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f"{user[0]['photo']}",
                             caption=profile_user(user=user, services=services, rating=rating),
                             reply_markup=keyboard)

    elif await postgres.check_rating_client(user_id=message.from_user.id):
        rating = await postgres.select_rating_client(user_id=message.from_user.id)
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f"{user[0]['photo']}",
                             caption=profile_user(user=user, services=services, rating=rating),
                             reply_markup=keyboard)

    else:
        rating = 0
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=f"{user[0]['photo']}",
                             caption=profile_user(user=user, services=services, rating=rating),
                             reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='✍️Редактировать свой профиль')
async def my_profile(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💻 Социальные сети', '💅 Услуги')
    keyboard.row('🙋‍♀️О себе', '🖼 Фото профиля')
    keyboard.row('📂 Мой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Чтобы повысить шанс выбора именно вас, заполните как можно больше информации',
                           reply_markup=keyboard)


@dp.message_handler(CheckClient(), text='✍️Редактировать свой профиль')
async def my_profile(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💻 Социальные сети', '💅 Стать мастером')
    keyboard.row('🙋‍♀️О себе', '🖼 Фото профиля')
    keyboard.row('📂 Мой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Чтобы повысить шанс выбора именно вас, заполните как можно больше информации',
                           reply_markup=keyboard)
