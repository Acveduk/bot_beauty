from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data.prolong_sub import prolong_sub
from filters import CheckUsers
from filters.check_user import CheckAdmin
from loader import dp, bot
from states.state_users import Register_user
from utils.db_api import postgres


@dp.message_handler(CommandStart(), CheckAdmin())
async def bot_start(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом', '👨‍💻 Админ')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Добро пожаловать. Бот создан для того, чтобы сводить мастеров и клиентов',
                           reply_markup=keyboard)

@dp.message_handler(CommandStart(), CheckUsers())
async def bot_start(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Добро пожаловать. Бот создан для того, чтобы сводить мастеров и клиентов',
                           reply_markup=keyboard)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('🌆 Москва', '🏙 Санкт-Петербург')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Для использования бота необходимо пройти регистрацию. \n'
                                '\n'
                                'Выберите город, нажав кнопку ниже',
                           reply_markup=keyboard)
    await Register_user.City.set()


@dp.message_handler(text=['🌆 Москва', '🏙 Санкт-Петербург'], state=Register_user.City)
async def set_user_name(message: types.Message, state: FSMContext):
    city = ''
    if message.text == '🌆 Москва':
        city += 'Москва'

    if message.text == '🏙 Санкт-Петербург':
        city += 'Санкт-Петербург'
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='📲 Отправить контакт', request_contact=True)
            ],
            [
                KeyboardButton(text='⬅️ назад')
            ]
        ],
        resize_keyboard=True
    )
    await state.update_data(city=city)
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Нажмите на кнопку ниже, чтобы отправить контакт",
                           reply_markup=keyboard)
    await Register_user.phone_number.set()


@dp.message_handler(content_types=types.ContentType.CONTACT, state=Register_user.phone_number)
async def master_start(message: types.Message, state: FSMContext):
    data = await state.get_data()
    city = data.get("city")
    phone_number = int(message.contact.phone_number)
    user_id = message.from_user.id
    name_user = message.from_user.full_name
    fio = 'Пусто'
    date_reg = datetime.now()
    photo = 'AgACAgIAAxkBAAInv2A7qRSh6NFGyVuxfUjLSgl-xUAnAAI4szEbsP_ZSaBdq-h_Hl8S0Kcjmy4AAwEAAwIAA20AA0uoAwABHgQ'
    metro = 'Пусто'
    address = 'Пусто'
    insta = 'Пусто'
    vk = 'Пусто'
    telegram = 'Пусто'
    about_me = 'Пусто'
    purse = -1
    manicure_pedicure = 'Пусто'
    hairdresser = 'Пусто'
    visage = 'Пусто'
    other_services = 'Пусто'
    favorites = -1
    await postgres.add_user_in_database(user_id=user_id, name_user=name_user, phone_number=phone_number, fio=fio,
                                        photo=photo, city=city, metro=metro, address=address, insta=insta, vk=vk,
                                        telegram=telegram, about_me=about_me, date_reg=date_reg, purse=purse,
                                        manicure_pedicure=manicure_pedicure, hairdresser=hairdresser, visage=visage, other_services=other_services, favorites=favorites)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')

    await message.answer(text=f"{message.from_user.full_name}, это ваше главное меню.\n"
                              f"Заполните ваш профиль и выберите быть мастером или клиентом", reply_markup=keyboard)
    await state.finish()
