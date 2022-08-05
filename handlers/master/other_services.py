from datetime import datetime

from aiogram import types

from data.prolong_sub import prolong_sub
from filters import CheckMaster
from keyboards.default.services import other_services_keyboard
from loader import dp, bot
from utils.db_api import postgres


@dp.message_handler(CheckMaster(), text='🧖‍♀️Другие услуги')
async def manicure_and_pedicure(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    sub = await postgres.get_sub_master(user_id=message.from_user.id)
    if sub[0]['other_services'] == 'Да':
        check_date_subscription = await postgres.check_date_sub_other_services(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                services_other_services = await postgres.check_other_services(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Нажмите на услугу, которую будете предоставлять в этом разделе',
                                       reply_markup=other_services_keyboard(
                                           services_other_services=services_other_services))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите или подключите вновь подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='💆‍♀️Массаж ❌')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_other_services(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_other_services(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_massage(user_id=message.from_user.id, massage='Да')
                services_other_services = await postgres.check_other_services(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы добавили услугу массаж',
                                       reply_markup=other_services_keyboard(
                                           services_other_services=services_other_services))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='👩‍⚕️Депиляция воском ❌')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_other_services(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_other_services(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_depilation_with_wax(user_id=message.from_user.id, depilation_with_wax='Да')
                services_other_services = await postgres.check_other_services(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы добавили услугу депиляция воском',
                                       reply_markup=other_services_keyboard(
                                           services_other_services=services_other_services))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='🧖‍♀️Шугаринг ❌')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_other_services(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_other_services(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_shugaring(user_id=message.from_user.id, shugaring='Да')
                services_other_services = await postgres.check_other_services(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы добавили услугу шугаринг',
                                       reply_markup=other_services_keyboard(
                                           services_other_services=services_other_services))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='🧴 Загар дома ❌')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_other_services(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_other_services(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_tan_at_home(user_id=message.from_user.id, tan_at_home='Да')
                services_other_services = await postgres.check_other_services(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы добавили услугу загар дома',
                                       reply_markup=other_services_keyboard(
                                           services_other_services=services_other_services))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='💆‍♀️Массаж ✅')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_other_services(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_other_services(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_massage(user_id=message.from_user.id, massage='Нет')
                services_other_services = await postgres.check_other_services(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы убрали услугу массаж',
                                       reply_markup=other_services_keyboard(
                                           services_other_services=services_other_services))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='👩‍⚕️Депиляция воском ✅')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_other_services(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_other_services(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_depilation_with_wax(user_id=message.from_user.id, depilation_with_wax='Нет')
                services_other_services = await postgres.check_other_services(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы убрали услугу депиляция воском',
                                       reply_markup=other_services_keyboard(
                                           services_other_services=services_other_services))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='🧖‍♀️Шугаринг ✅')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_other_services(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_other_services(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_shugaring(user_id=message.from_user.id, shugaring='Нет')
                services_other_services = await postgres.check_other_services(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы убрали услугу шугаринг',
                                       reply_markup=other_services_keyboard(
                                           services_other_services=services_other_services))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)


@dp.message_handler(CheckMaster(), text='🧴 Загар дома ✅')
async def manicure_and_pedicure(message: types.Message):
    if await postgres.check_master_in_other_services(user_id=message.from_user.id):
        check_date_subscription = await postgres.check_date_sub_other_services(user_id=message.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_tan_at_home(user_id=message.from_user.id, tan_at_home='Нет')
                services_other_services = await postgres.check_other_services(user_id=message.from_user.id)
                await bot.send_message(chat_id=message.from_user.id,
                                       text='Вы убрали услугу загар дома',
                                       reply_markup=other_services_keyboard(
                                           services_other_services=services_other_services))

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('💅 Маникюр/Педикюр', '💇‍♀️Парикмахер')
        keyboard.row('💋 Визаж', '🧖‍♀️Другие услуги')
        keyboard.row('✍️Редактировать свой профиль')
        await bot.send_message(chat_id=message.from_user.id,
                               text='Оформите подписку в разделе кошелек',
                               reply_markup=keyboard)
