from datetime import datetime

from aiogram import types

from data.prolong_sub import prolong_sub
from filters import CheckMaster
from keyboards.default.services import visage_keyboard
from loader import dp, bot
from utils.db_api import postgres


@dp.message_handler(CheckMaster(), text='💋 Визаж')
async def manicure_and_pedicure(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    sub = await postgres.get_sub_master(user_id=message.from_user.id)
    if sub[0]['visage'] == 'Да':
        if await postgres.check_master_in_visage(user_id=message.from_user.id):
            check_date_subscription = await postgres.check_date_sub_visage(user_id=message.from_user.id)
            for check_date in check_date_subscription:
                if datetime.now() <= check_date['date_end']:
                    services_visage = await postgres.check_visage(user_id=message.from_user.id)
                    await bot.send_message(chat_id=message.from_user.id,
                                           text='Нажмите на услугу, которую будете предоставлять в этом разделе',
                                           reply_markup=visage_keyboard(services_visage=services_visage))
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите или подключите вновь подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='💋 Макияж ❌')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_visage(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_visage(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_makeup(user_id=message.from_user.id, makeup='Да')
                services_visage = await postgres.check_visage(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы добавили услугу макияж',
                                       reply_markup=visage_keyboard(services_visage=services_visage))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='💋 Макияж ✅')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_visage(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_visage(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_makeup(user_id=message.from_user.id, makeup='Нет')
                services_visage = await postgres.check_visage(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы убрали услугу макияж',
                                       reply_markup=visage_keyboard(services_visage=services_visage))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='👁 Брови ❌')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_visage(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_visage(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_eyebrows(user_id=message.from_user.id, eyebrows='Да')
                services_visage = await postgres.check_visage(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы добавили услугу брови',
                                       reply_markup=visage_keyboard(services_visage=services_visage))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='👁 Брови ✅')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_visage(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_visage(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_eyebrows(user_id=message.from_user.id, eyebrows='Нет')
                services_visage = await postgres.check_visage(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы убрали услугу брови',
                                       reply_markup=visage_keyboard(services_visage=services_visage))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='👀 Ресницы ❌')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_visage(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_visage(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_eyelashes(user_id=message.from_user.id, eyelashes='Да')
                services_visage = await postgres.check_visage(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы добавили услугу ресницы',
                                       reply_markup=visage_keyboard(services_visage=services_visage))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='👀 Ресницы ✅')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_visage(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_visage(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_eyelashes(user_id=message.from_user.id, eyelashes='Нет')
                services_visage = await postgres.check_visage(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы убрали услугу ресницы',
                                       reply_markup=visage_keyboard(services_visage=services_visage))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='👰‍ Свадебный образ ❌')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_visage(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_visage(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_wedding_image(user_id=message.from_user.id, wedding_image='Да')
                services_visage = await postgres.check_visage(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы добавили услугу свадебный образ',
                                       reply_markup=visage_keyboard(services_visage=services_visage))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='👰‍ Свадебный образ ✅')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_visage(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_visage(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_wedding_image(user_id=message.from_user.id, wedding_image='Нет')
                services_visage = await postgres.check_visage(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы убрали услугу свадебный образ',
                                       reply_markup=visage_keyboard(services_visage=services_visage))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)
