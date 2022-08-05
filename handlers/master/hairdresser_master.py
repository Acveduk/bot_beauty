from datetime import datetime

from aiogram import types

from data.prolong_sub import prolong_sub
from filters import CheckMaster
from keyboards.default.services import hairdresser_keyboard
from loader import dp, bot
from utils.db_api import postgres


@dp.message_handler(CheckMaster(), text='💇‍♀️Парикмахер')
async def manicure_and_pedicure(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    sub = await postgres.get_sub_master(user_id=message.from_user.id)
    if sub[0]['hairdresser'] == 'Да':
        check_date_subscription = await postgres.check_date_sub_hairdresser(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                services_hairdresser = await postgres.check_hairdresser(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Нажмите на услугу, которую будете предоставлять в этом разделе',
                                       reply_markup=hairdresser_keyboard(services_hairdresser=services_hairdresser))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите или подключите вновь подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='💇‍♀️Стрижка ❌')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_hairdresser(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_hairdresser(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_haircut(user_id=message.from_user.id, haircut='Да')
                services_hairdresser = await postgres.check_hairdresser(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы добавили услугу стрижка',
                                       reply_markup=hairdresser_keyboard(services_hairdresser=services_hairdresser))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='💇‍♀️Стрижка ✅')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_hairdresser(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_hairdresser(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_haircut(user_id=message.from_user.id, haircut='Нет')
                services_hairdresser = await postgres.check_hairdresser(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы убрали услугу стрижка',
                                       reply_markup=hairdresser_keyboard(services_hairdresser=services_hairdresser))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='💇‍♂️Мужская стрижка ❌')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_hairdresser(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_hairdresser(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_man_haircut(user_id=message.from_user.id, man_haircut='Да')
                services_hairdresser = await postgres.check_hairdresser(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы добавили услугу мужская стрижка',
                                       reply_markup=hairdresser_keyboard(services_hairdresser=services_hairdresser))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='💇‍♂️Мужская стрижка ✅')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_hairdresser(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_hairdresser(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_man_haircut(user_id=message.from_user.id, man_haircut='Нет')
                services_hairdresser = await postgres.check_hairdresser(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы убрали услугу мужская стрижка',
                                       reply_markup=hairdresser_keyboard(services_hairdresser=services_hairdresser))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='💆‍♀️Укладка и прически ❌')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_hairdresser(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_hairdresser(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_hair_styling(user_id=message.from_user.id, hair_styling='Да')
                services_hairdresser = await postgres.check_hairdresser(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы добавили услугу укладка и прически',
                                       reply_markup=hairdresser_keyboard(services_hairdresser=services_hairdresser))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='💆‍♀️Укладка и прически ✅')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_hairdresser(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_hairdresser(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_hair_styling(user_id=message.from_user.id, hair_styling='Нет')
                services_hairdresser = await postgres.check_hairdresser(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы убрали услугу укладка и прически',
                                       reply_markup=hairdresser_keyboard(services_hairdresser=services_hairdresser))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='👩‍🦰 Окрашивание ❌')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_hairdresser(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_hairdresser(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_hair_coloring(user_id=message.from_user.id, hair_coloring='Да')
                services_hairdresser = await postgres.check_hairdresser(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы добавили услугу окрашивание',
                                       reply_markup=hairdresser_keyboard(services_hairdresser=services_hairdresser))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='👩‍🦰 Окрашивание ✅')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_hairdresser(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_hairdresser(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_hair_coloring(user_id=message.from_user.id, hair_coloring='Нет')
                services_hairdresser = await postgres.check_hairdresser(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы убрали услугу окрашивание',
                                       reply_markup=hairdresser_keyboard(services_hairdresser=services_hairdresser))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='👩‍⚕️Уход и лечение ❌')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_hairdresser(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_hairdresser(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_hair_care(user_id=message.from_user.id, hair_care='Да')
                services_hairdresser = await postgres.check_hairdresser(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы добавили услугу уход и лечение',
                                       reply_markup=hairdresser_keyboard(services_hairdresser=services_hairdresser))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='👩‍⚕️Уход и лечение ✅')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_hairdresser(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_hairdresser(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_hair_care(user_id=message.from_user.id, hair_care='Нет')
                services_hairdresser = await postgres.check_hairdresser(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы убрали услугу уход и лечение',
                                       reply_markup=hairdresser_keyboard(services_hairdresser=services_hairdresser))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)
