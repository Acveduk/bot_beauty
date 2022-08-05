from aiogram import types
from aiogram.dispatcher import FSMContext

from data.prolong_sub import prolong_sub
from filters import CheckUsers
from loader import dp, bot
from states.state_users import Metro, Create
from utils.db_api import postgres


@dp.message_handler(CheckUsers(), text='📝 Создать заявку на услугу')
async def create(message: types.Message, state: FSMContext):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ Отмена')
    city = await postgres.select_city(user_id=message.from_user.id)
    await state.update_data(city=city[0]['city'])
    await bot.send_message(chat_id=message.from_user.id,
                           text='Для составлении заявки вам надо указать: \n\n'
                                '✅ Станцию метро\n'
                                '✅ Услугу\n'
                                '✅ Дату и время\n'
                                '✅ Описание усуги\n'
                                '✅ Фото примера работы')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Введите станцию метро',
                           reply_markup=keyboard)

    await Create.metro.set()


@dp.message_handler(text='⬅️ Отмена', state=Create.metro)
async def services(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы вернулись в меню',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(state=Create.metro)
async def metro(message: types.Message, state: FSMContext):
    metro = message.text
    await state.update_data(metro=metro)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
    keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно ввели станцию метро.\n'
                                'Выберите вид услуги, которую хотите получить', reply_markup=keyboard)
    await Create.services.set()


@dp.message_handler(text='⬅️ Назад', state=Create.services)
async def services(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Введите станцию метро',
                           reply_markup=keyboard)
    await Create.metro.set()

@dp.message_handler(text='Отмена', state=Create.services)
async def services(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы вернулись в меню',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(text='💅 Маникюр/Педикюр', state=Create.services)
async def metro(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('🖐 Маникюр', '🦶 Педикюр')
    keyboard.row('💅 Услуги')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите услугу, которую хотите получить', reply_markup=keyboard)
    await Create.services.set()

@dp.message_handler(text='💅 Услуги', state=Create.services)
async def services(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
    keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите вид услуги, которую хотите получить',
                           reply_markup=keyboard)
    await Create.services.set()

@dp.message_handler(text='🖐 Маникюр', state=Create.services)
async def metro(message: types.Message, state: FSMContext):
    service = 'Маникюр'
    await state.update_data(service=service)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно выбрали услугу\n'
                                'Введите желаемую дату и время оказания услуги',
                           reply_markup=keyboard)
    await Create.date_time.set()


@dp.message_handler(text='🦶 Педикюр', state=Create.services)
async def metro(message: types.Message, state: FSMContext):
    service = 'Педикюр'
    await state.update_data(service=service)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно выбрали услугу\n'
                                'Введите желаемую дату и время оказания услуги',
                           reply_markup=keyboard)
    await Create.date_time.set()


@dp.message_handler(text='💇‍♀️Парикмахер', state=Create.services)
async def metro(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💇‍♀️Стрижка', '💇‍♂️Мужская стрижка')
    keyboard.row('💆‍♀️Укладка и прически', '👩‍🦰 Окрашивание')
    keyboard.row('👩‍⚕️Уход и лечение')
    keyboard.row('💅 Услуги')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите услугу, которую хотите получить', reply_markup=keyboard)
    await Create.services.set()


@dp.message_handler(text='💇‍♀️Стрижка', state=Create.services)
async def metro(message: types.Message, state: FSMContext):
    service = 'Стрижка'
    await state.update_data(service=service)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно выбрали услугу\n'
                                'Введите желаемую дату и время оказания услуги',
                           reply_markup=keyboard)
    await Create.date_time.set()


@dp.message_handler(text='💇‍♂️Мужская стрижка', state=Create.services)
async def metro(message: types.Message, state: FSMContext):
    service = 'Мужская стрижка'
    await state.update_data(service=service)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно выбрали услугу\n'
                                'Введите желаемую дату и время оказания услуги',
                           reply_markup=keyboard)
    await Create.date_time.set()


@dp.message_handler(text='💆‍♀️Укладка и прически', state=Create.services)
async def metro(message: types.Message, state: FSMContext):
    service = 'Укладка и прически'
    await state.update_data(service=service)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно выбрали услугу\n'
                                'Введите желаемую дату и время оказания услуги',
                           reply_markup=keyboard)
    await Create.date_time.set()


@dp.message_handler(text='👩‍🦰 Окрашивание', state=Create.services)
async def metro(message: types.Message, state: FSMContext):
    service = 'Окрашивание'
    await state.update_data(service=service)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно выбрали услугу\n'
                                'Введите желаемую дату и время оказания услуги',
                           reply_markup=keyboard)
    await Create.date_time.set()


@dp.message_handler(text='👩‍⚕️Уход и лечение', state=Create.services)
async def metro(message: types.Message, state: FSMContext):
    service = 'Уход и лечение'
    await state.update_data(service=service)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно выбрали услугу\n'
                                'Введите желаемую дату и время оказания услуги',
                           reply_markup=keyboard)
    await Create.date_time.set()


@dp.message_handler(text='💋 Визаж', state=Create.services)
async def metro(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💋 Макияж', '👁 Брови')
    keyboard.row('👀 Ресницы', '👰‍ Свадебный образ')
    keyboard.row('💅 Услуги')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите услугу, которую хотите получить', reply_markup=keyboard)
    await Create.services.set()


@dp.message_handler(text='💋 Макияж', state=Create.services)
async def metro(message: types.Message, state: FSMContext):
    service = 'Макияж'
    await state.update_data(service=service)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно выбрали услугу\n'
                                'Введите желаемую дату и время оказания услуги',
                           reply_markup=keyboard)
    await Create.date_time.set()


@dp.message_handler(text='👁 Брови', state=Create.services)
async def metro(message: types.Message, state: FSMContext):
    service = 'Брови'
    await state.update_data(service=service)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно выбрали услугу\n'
                                'Введите желаемую дату и время оказания услуги',
                           reply_markup=keyboard)
    await Create.date_time.set()


@dp.message_handler(text='👀 Ресницы', state=Create.services)
async def metro(message: types.Message, state: FSMContext):
    service = 'Ресницы'
    await state.update_data(service=service)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно выбрали услугу\n'
                                'Введите желаемую дату и время оказания услуги',
                           reply_markup=keyboard)
    await Create.date_time.set()


@dp.message_handler(text='👰‍ Свадебный образ', state=Create.services)
async def metro(message: types.Message, state: FSMContext):
    service = 'Свадебный образ'
    await state.update_data(service=service)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно выбрали услугу\n'
                                'Введите желаемую дату и время оказания услуги',
                           reply_markup=keyboard)
    await Create.date_time.set()


@dp.message_handler(text='🧖‍♀️Другие услуги', state=Create.services)
async def metro(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💆‍♀️Массаж', '👩‍⚕️Депиляция воском')
    keyboard.row('🧖‍♀️Шугаринг', '🧴 Загар дома')
    keyboard.row('💅 Услуги')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите услугу, которую хотите получить', reply_markup=keyboard)
    await Create.services.set()


@dp.message_handler(text='💆‍♀️Массаж', state=Create.services)
async def metro(message: types.Message, state: FSMContext):
    service = 'Массаж'
    await state.update_data(service=service)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно выбрали услугу\n'
                                'Введите желаемую дату и время оказания услуги',
                           reply_markup=keyboard)
    await Create.date_time.set()


@dp.message_handler(text='👩‍⚕️Депиляция воском', state=Create.services)
async def metro(message: types.Message, state: FSMContext):
    service = 'Депиляция воском'
    await state.update_data(service=service)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно выбрали услугу\n'
                                'Введите желаемую дату и время оказания услуги',
                           reply_markup=keyboard)
    await Create.date_time.set()


@dp.message_handler(text='🧖‍♀️Шугаринг', state=Create.services)
async def metro(message: types.Message, state: FSMContext):
    service = 'Шугаринг'
    await state.update_data(service=service)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно выбрали услугу\n'
                                'Введите желаемую дату и время оказания услуги',
                           reply_markup=keyboard)
    await Create.date_time.set()


@dp.message_handler(text='🧴 Загар дома', state=Create.services)
async def metro(message: types.Message, state: FSMContext):
    service = 'Загар дома'
    await state.update_data(service=service)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно выбрали услугу\n'
                                'Введите желаемую дату и время оказания услуги',
                           reply_markup=keyboard)
    await Create.date_time.set()


@dp.message_handler(text='⬅️ Назад', state=Create.date_time)
async def services(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
    keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите вид услуги, которую хотите получить',
                           reply_markup=keyboard)
    await Create.services.set()

@dp.message_handler(text='Отмена', state=Create.date_time)
async def services(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы вернулись в меню',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(state=Create.date_time)
async def date_time(message: types.Message, state: FSMContext):
    date_time = message.text
    await state.update_data(date_time=date_time)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно ввели желаймое время\n'
                                'Опишите услугу, которую хотите получить',
                           reply_markup=keyboard)
    await Create.description.set()


@dp.message_handler(text='⬅️ Назад', state=Create.description)
async def services(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ Назад', 'Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Введите желаемую дату и время оказания услуги',
                           reply_markup=keyboard)
    await Create.date_time.set()

@dp.message_handler(text='Отмена', state=Create.description)
async def services(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы вернулись в меню',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(state=Create.description)
async def description(message: types.Message, state: FSMContext):
    description = message.text
    await state.update_data(description=description)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⏩ Пропустить')
    keyboard.row('Отмена')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно ввели описание услуги\n'
                                'Прикрипите фото для примера',
                           reply_markup=keyboard)
    await Create.photo.set()


@dp.message_handler(text='Отмена', state=Create.photo)
async def services(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы вернулись в меню заявок',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(content_types=types.ContentType.PHOTO, state=Create.photo)
async def photo(message: types.Message, state: FSMContext):
    await message.photo[-1].download()
    photo_id = message.photo[-1].file_id
    data = await state.get_data()
    city = data.get("city")
    metro = data.get("metro")
    service = data.get("service")
    date_time = data.get("date_time")
    description = data.get("description")
    name = message.from_user.id
    await postgres.add_applications(user_id=message.from_user.id, city=city, metro=metro, service=service,
                                    date_time=date_time, description=description, photo=photo_id, name=name)
    number = await postgres.select_number_applications(user_id=message.from_user.id)
    # photo = await postgres.select_photo(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')

    await bot.send_photo(chat_id=message.from_user.id, photo=photo_id,
                         caption=f"❗️Номер заявки: #a{number[0]['max']}\n\n"
                                 f"👤 Пользователь: <a href='tg://user?id={message.from_user.id}'><b>{message.from_user.full_name}</b></a>\n\n"
                                 f"💅 Услуга: {service}\n\n"
                                 f"🏙 Город: {city}\n"
                                 f"🚇 Метро: {metro}\n\n"
                                 f"🕐 Желаемая дата: {date_time}\n\n"
                                 f"🗒 Описание заявки: {description}", reply_markup=keyboard)

    await bot.send_photo(chat_id="@poisk_mastera", photo=photo_id,
                         caption=f"#a{number[0]['max']}\n\n"
                                 f"👤 Пользователь: <a href='tg://user?id={message.from_user.id}'><b>{message.from_user.full_name}</b></a>\n\n"
                                 f"💅 Услуга: {service}\n\n"
                                 f"🏙 Город: {city}\n"
                                 f"🚇 Метро: {metro}\n\n"
                                 f"🕐 Желаемая дата: {date_time}\n\n"
                                 f"🗒 Описание заявки: {description}")
    await state.finish()


@dp.message_handler(text='⏩ Пропустить', state=Create.photo)
async def photo(message: types.Message, state: FSMContext):
    data = await state.get_data()
    city = data.get("city")
    metro = data.get("metro")
    service = data.get("service")
    date_time = data.get("date_time")
    description = data.get("description")
    name = message.from_user.full_name
    await postgres.add_applications(user_id=message.from_user.id, city=city, metro=metro, service=service,
                                    date_time=date_time, description=description, photo='Пусто', name=name)
    number = await postgres.select_number_applications(user_id=message.from_user.id)
    # photo = await postgres.select_photo(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"❗️Номер заявки: #з{number[0]['max']}\n\n"
                                f"👤 Пользователь: <a href='tg://user?id={message.from_user.id}'><b>{message.from_user.full_name}</b></a>\n\n"
                                f"💅 Услуга: {service}\n\n"
                                f"🏙 Город: {city}\n"
                                f"🚇 Метро: {metro}\n\n"
                                f"🕐 Желаемая дата: {date_time}\n\n"
                                f"🗒 Описание заявки: {description}", reply_markup=keyboard)

    await bot.send_message(chat_id="@poisk_mastera",
                           text=f"#з{number[0]['max']}\n\n"
                                f"👤 Пользователь: <a href='tg://user?id={message.from_user.id}'><b>{message.from_user.full_name}</b></a>\n\n"
                                f"💅 Услуга: {service}\n\n"
                                f"🏙 Город: {city}\n"
                                f"🚇 Метро: {metro}\n\n"
                                f"🕐 Желаемая дата: {date_time}\n\n"
                                f"🗒 Описание заявки: {description}")
    await state.finish()
