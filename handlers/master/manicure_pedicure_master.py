from datetime import datetime

from aiogram import types

from data.prolong_sub import prolong_sub
from filters import CheckMaster
from keyboards.default.services import manicure_keyboard
from loader import dp, bot
from utils.db_api import postgres


@dp.message_handler(CheckMaster(), text='💅 Маникюр/Педикюр')
async def manicure_and_pedicure(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    sub = await postgres.get_sub_master(user_id=message.from_user.id)
    if sub[0]['manicure_pedicure'] == 'Да':
        check_date_subscription = await postgres.check_date_sub_manicure_pedicure(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                services_manicure = await postgres.check_manicure(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Нажмите на услугу, которую будете предоставлять в этом разделе',
                                       reply_markup=manicure_keyboard(services_manicure=services_manicure))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите или подключите вновь подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='🖐 Маникюр ❌')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_manicure(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_manicure_pedicure(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_manicure(user_id=message.from_user.id, manicure='Да')
                services_manicure = await postgres.check_manicure(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы добавили услугу маникюр',
                                       reply_markup=manicure_keyboard(services_manicure=services_manicure))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='🦶 Педикюр ❌')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_manicure(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_manicure_pedicure(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_pedicure(user_id=message.from_user.id, pedicure='Да')
                services_manicure = await postgres.check_manicure(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы добавили услугу педикюр',
                                       reply_markup=manicure_keyboard(services_manicure=services_manicure))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='🖐 Маникюр ✅')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_manicure(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_manicure_pedicure(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_manicure(user_id=message.from_user.id, manicure='Нет')
                services_manicure = await postgres.check_manicure(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы убрали услугу маникюр',
                                       reply_markup=manicure_keyboard(services_manicure=services_manicure))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='🦶 Педикюр ✅')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_manicure(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_manicure_pedicure(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_pedicure(user_id=message.from_user.id, pedicure='Нет')
                services_manicure = await postgres.check_manicure(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы убрали услугу педикюр',
                                       reply_markup=manicure_keyboard(services_manicure=services_manicure))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)
