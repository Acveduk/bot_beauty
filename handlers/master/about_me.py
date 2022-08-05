from aiogram import types
from aiogram.dispatcher import FSMContext

from data.prolong_sub import prolong_sub
from filters import CheckUsers
from loader import dp, bot
from states.state_users import City, Address, Fio, About_me, Metro
from utils.db_api import postgres


@dp.message_handler(CheckUsers(), text='🙋‍♀️О себе')
async def about_me(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('🚇 Метро', '🏡 Адрес')
    keyboard.row('🖼 О себе', '👤 ФИО')
    keyboard.row('✍️Редактировать свой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Чтобы повысить шанс выбора именно вас, заполните как можно больше информации',
                           reply_markup=keyboard)


# @dp.message_handler(CheckUsers(), text='🏙 Город')
# async def city(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.row('⬅️ назад')
#
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Введите ваш город, так клиентам будет проще вас найти',
#                            reply_markup=keyboard)
#
#     await City.city_master.set()
#
#
# @dp.message_handler(CheckUsers(), text='⬅️ назад', state=City.city_master)
# async def back(message: types.Message, state: FSMContext):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.row('🏙 Город', '🏡 Адрес')
#     keyboard.row('🖼 О себе', '👤 ФИО', '🚇 Метро')
#     keyboard.row('✍️Редактировать свой профиль')
#
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Вы вернулись в меню редактирования профиля',
#                            reply_markup=keyboard)
#     await state.finish()
#
#
# @dp.message_handler(CheckUsers(), state=City.city_master)
# async def city_master(message: types.Message, state: FSMContext):
#     city_master = message.text
#     user_id = message.from_user.id
#     await postgres.update_city(user_id=user_id, city=city_master)
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.row('🏙 Город', '🏡 Адрес')
#     keyboard.row('🖼 О себе', '👤 ФИО', '🚇 Метро')
#     keyboard.row('✍️Редактировать свой профиль')
#
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Вы успешно обновили ваш город',
#                            reply_markup=keyboard)
#     await state.finish()


@dp.message_handler(CheckUsers(), text='🏡 Адрес')
async def address(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ назад')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Введите ваш адрес, где вы работаете',
                           reply_markup=keyboard)

    await Address.address_master.set()


@dp.message_handler(CheckUsers(), text='⬅️ назад', state=Address.address_master)
async def back(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('🚇 Метро', '🏡 Адрес')
    keyboard.row('🖼 О себе', '👤 ФИО')
    keyboard.row('✍️Редактировать свой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы вернулись в меню редактирования профиля',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(CheckUsers(), state=Address.address_master)
async def address_master(message: types.Message, state: FSMContext):
    address_master = message.text
    user_id = message.from_user.id
    await postgres.update_address(user_id=user_id, address=address_master)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('🚇 Метро', '🏡 Адрес')
    keyboard.row('🖼 О себе', '👤 ФИО')
    keyboard.row('✍️Редактировать свой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно обновили ваш адрес работы',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(CheckUsers(), text='👤 ФИО')
async def fio(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ назад')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Введите ваше ФИО',
                           reply_markup=keyboard)

    await Fio.fio_master.set()


@dp.message_handler(CheckUsers(), text='⬅️ назад', state=Fio.fio_master)
async def back(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('🚇 Метро', '🏡 Адрес')
    keyboard.row('🖼 О себе', '👤 ФИО')
    keyboard.row('✍️Редактировать свой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы вернулись в меню редактирования профиля',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(CheckUsers(), state=Fio.fio_master)
async def fio_master(message: types.Message, state: FSMContext):
    fio_master = message.text
    user_id = message.from_user.id
    await postgres.update_fio(user_id=user_id, fio=fio_master)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('🚇 Метро', '🏡 Адрес')
    keyboard.row('🖼 О себе', '👤 ФИО')
    keyboard.row('✍️Редактировать свой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно обновили ваше ФИО',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(CheckUsers(), text='🖼 О себе')
async def about_me(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ назад')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Введите информацию о себе, которая опишет вас как мастера',
                           reply_markup=keyboard)

    await About_me.about_me_master.set()


@dp.message_handler(CheckUsers(), text='⬅️ назад', state=About_me.about_me_master)
async def back(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('🚇 Метро', '🏡 Адрес')
    keyboard.row('🖼 О себе', '👤 ФИО')
    keyboard.row('✍️Редактировать свой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы вернулись в меню редактирования профиля',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(CheckUsers(), state=About_me.about_me_master)
async def about_me_master(message: types.Message, state: FSMContext):
    about_me_master = message.text
    user_id = message.from_user.id
    await postgres.update_about_me(user_id=user_id, about_me=about_me_master)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('🚇 Метро', '🏡 Адрес')
    keyboard.row('🖼 О себе', '👤 ФИО')
    keyboard.row('✍️Редактировать свой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно обновили информацию о себе',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(CheckUsers(), text='🚇 Метро')
async def metro(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ назад')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Введите ближайшую к вам станцию метро',
                           reply_markup=keyboard)

    await Metro.metro.set()


@dp.message_handler(CheckUsers(), text='⬅️ назад', state=Metro.metro)
async def back(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('🚇 Метро', '🏡 Адрес')
    keyboard.row('🖼 О себе', '👤 ФИО')
    keyboard.row('✍️Редактировать свой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы вернулись в меню редактирования профиля',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(CheckUsers(), state=Metro.metro)
async def fio_master(message: types.Message, state: FSMContext):
    metro_master = message.text
    user_id = message.from_user.id
    await postgres.update_metro(user_id=user_id, metro=metro_master)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('🚇 Метро', '🏡 Адрес')
    keyboard.row('🖼 О себе', '👤 ФИО')
    keyboard.row('✍️Редактировать свой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно обновили информацию о ближайшей к вам станции метро',
                           reply_markup=keyboard)
    await state.finish()
