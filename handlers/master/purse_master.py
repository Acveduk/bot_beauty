from datetime import datetime, timedelta

from aiogram import types
from aiogram.types import InlineKeyboardButton

from data.prolong_sub import prolong_sub
from filters import CheckUsers, PurseClient, PurseMaster, CheckMaster
from keyboards.inline.sub import sub_keyboard
from loader import dp, bot
from utils.db_api import postgres


@dp.message_handler(CheckUsers(), CheckMaster(), PurseMaster(), text='💰 Кошелек')
async def purse(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    purse_master = await postgres.purse(user_id=message.from_user.id)
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='💳 Пополнить кошелек', callback_data='replenish')
            ],
            [
                InlineKeyboardButton(text='📝 Управление подпиской', callback_data='subscription')
            ],
            [
                InlineKeyboardButton(text='💶 Донат', callback_data='donation')
            ]
        ]
    )
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"В вашем кошельке: {purse_master[0]['purse']} руб",
                           reply_markup=keyboard)


@dp.message_handler(CheckUsers(), PurseClient(), text='💰 Кошелек')
async def purse_client(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='💶 Донат', callback_data='donation')
            ]
        ]
    )
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Тут вы можете поддержать создателей бота",
                           reply_markup=keyboard)


@dp.callback_query_handler(text='subscription')
async def sub(call: types.CallbackQuery):
    services = await postgres.get_sub_master(user_id=call.from_user.id)
    await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))


@dp.callback_query_handler(text='manicure-')
async def sub(call: types.CallbackQuery):
    purse_master = await postgres.purse(user_id=call.from_user.id)
    null = 0
    purse = int(purse_master[0]['purse']) - 100
    if purse < null:
        if await postgres.check_master_in_manicure(user_id=call.from_user.id):
            check_date_subscription = await postgres.check_date_sub_manicure_pedicure(user_id=call.from_user.id)
            for check_date in check_date_subscription:
                if datetime.now() <= check_date['date_end']:
                    keyboard = types.InlineKeyboardMarkup(
                        inline_keyboard=[
                            [
                                InlineKeyboardButton(text=f'Подтвердить', callback_data=f'manicure_yes:{purse}')
                            ],
                            [
                                InlineKeyboardButton(text=f'Отмена', callback_data=f'manicure_no')
                            ]
                        ]
                    )
                    await call.message.edit_reply_markup(reply_markup=keyboard)

                else:
                    await bot.send_message(chat_id=call.from_user.id,
                                           text=f"Недостаточно средств. Баланс вашего кошелька: {purse_master[0]['purse']} руб")

        else:
            await bot.send_message(chat_id=call.from_user.id,
                                   text=f"Недостаточно средств. Баланс вашего кошелька: {purse_master[0]['purse']} руб")

    else:
        keyboard = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f'Подтвердить', callback_data=f'manicure_yes:{purse}')
                ],
                [
                    InlineKeyboardButton(text=f'Отмена', callback_data=f'manicure_no')
                ]
            ]
        )
        await call.message.edit_reply_markup(reply_markup=keyboard)


@dp.callback_query_handler(text_contains='manicure_yes')
async def confirm(call: types.CallbackQuery):
    if await postgres.check_master_in_manicure(user_id=call.from_user.id):
        check_date_subscription = await postgres.check_date_sub_manicure_pedicure(user_id=call.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_sub_manicure(user_id=call.from_user.id, manicure_pedicure='Да')
                services = await postgres.get_sub_master(user_id=call.from_user.id)
                await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
                await bot.send_message(chat_id=call.from_user.id,
                                       text=f"Улуга активирована.")

            else:
                purse_back = call.data.split(":")[-1]
                purse = int(purse_back)
                date_start = datetime.now()
                date_end = date_start + timedelta(days=30)
                await postgres.subscribe(user_id=call.from_user.id, purse=purse)
                await postgres.update_sub_manicure(user_id=call.from_user.id, manicure_pedicure='Да')
                await postgres.update_date_sub_manicure(user_id=call.from_user.id, date_start=date_start,
                                                        date_end=date_end)
                services = await postgres.get_sub_master(user_id=call.from_user.id)
                await call.message.edit_text(text=f"В вашем кошельке: {purse} руб")
                await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
                await bot.send_message(chat_id=call.from_user.id,
                                       text=f"Подписка успешно оформлена. Баланс вашего кошелька: {purse} руб")
    else:
        purse_back = call.data.split(":")[-1]
        purse = int(purse_back)
        date_start = datetime.now()
        date_end = date_start + timedelta(days=30)
        manicure = 'Нет'
        pedicure = 'Нет'
        await postgres.add_master_in_manicure(user_id=call.from_user.id, manicure=manicure, pedicure=pedicure,
                                              date_start=date_start, date_end=date_end)
        await postgres.subscribe(user_id=call.from_user.id, purse=purse)
        await postgres.update_sub_manicure(user_id=call.from_user.id, manicure_pedicure='Да')
        services = await postgres.get_sub_master(user_id=call.from_user.id)
        await call.message.edit_text(text=f"В вашем кошельке: {purse} руб")
        await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
        await bot.send_message(chat_id=call.from_user.id,
                               text=f"Подписка успешно оформлена. Баланс вашего кошелька: {purse} руб")


@dp.callback_query_handler(text='manicure_no')
async def cancel_sub(call: types.CallbackQuery):
    services = await postgres.get_sub_master(user_id=call.from_user.id)
    await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))


@dp.callback_query_handler(text='hairdresser-')
async def sub(call: types.CallbackQuery):
    purse_master = await postgres.purse(user_id=call.from_user.id)
    null = 0
    purse = int(purse_master[0]['purse']) - 100
    if purse < null:
        if await postgres.check_master_in_hairdresser(user_id=call.from_user.id):
            check_date_subscription = await postgres.check_date_sub_hairdresser(user_id=call.from_user.id)
            for check_date in check_date_subscription:
                if datetime.now() <= check_date['date_end']:
                    keyboard = types.InlineKeyboardMarkup(
                        inline_keyboard=[
                            [
                                InlineKeyboardButton(text=f'Подтвердить', callback_data=f'hairdresser_yes:{purse}')
                            ],
                            [
                                InlineKeyboardButton(text=f'Отмена', callback_data=f'hairdresser_no')
                            ]
                        ]
                    )
                    await call.message.edit_reply_markup(reply_markup=keyboard)

                else:
                    await bot.send_message(chat_id=call.from_user.id,
                                           text=f"Недостаточно средств. Баланс вашего кошелька: {purse_master[0]['purse']} руб")
        else:
            await bot.send_message(chat_id=call.from_user.id,
                                   text=f"Недостаточно средств. Баланс вашего кошелька: {purse_master[0]['purse']} руб")

    else:
        keyboard = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f'Подтвердить', callback_data=f'hairdresser_yes:{purse}')
                ],
                [
                    InlineKeyboardButton(text=f'Отмена', callback_data=f'hairdresser_no')
                ]
            ]
        )
        await call.message.edit_reply_markup(reply_markup=keyboard)


@dp.callback_query_handler(text_contains='hairdresser_yes')
async def confirm(call: types.CallbackQuery):
    if await postgres.check_master_in_hairdresser(user_id=call.from_user.id):
        check_date_subscription = await postgres.check_date_sub_hairdresser(user_id=call.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_sub_hairdresser(user_id=call.from_user.id, hairdresser='Да')
                services = await postgres.get_sub_master(user_id=call.from_user.id)
                await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
                await bot.send_message(chat_id=call.from_user.id,
                                       text=f"Улуга активирована.")

            else:
                purse_back = call.data.split(":")[-1]
                purse = int(purse_back)
                date_start = datetime.now()
                date_end = date_start + timedelta(days=30)
                await postgres.subscribe(user_id=call.from_user.id, purse=purse)
                await postgres.update_sub_hairdresser(user_id=call.from_user.id, hairdresser='Да')
                await postgres.update_date_sub_hairdresser(user_id=call.from_user.id, date_start=date_start,
                                                           date_end=date_end)
                services = await postgres.get_sub_master(user_id=call.from_user.id)
                await call.message.edit_text(text=f"В вашем кошельке: {purse} руб")
                await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
                await bot.send_message(chat_id=call.from_user.id,
                                       text=f"Подписка успешно оформлена. Баланс вашего кошелька: {purse} руб")

    else:
        purse_back = call.data.split(":")[-1]
        purse = int(purse_back)
        date_start = datetime.now()
        date_end = date_start + timedelta(days=30)
        haircut = 'Нет'
        man_haircut = 'Нет'
        hair_styling = 'Нет'
        hair_coloring = 'Нет'
        hair_care = 'Нет'
        await postgres.add_master_in_hairdresser(user_id=call.from_user.id, haircut=haircut, man_haircut=man_haircut,
                                                 hair_styling=hair_styling, hair_coloring=hair_coloring,
                                                 hair_care=hair_care, date_start=date_start, date_end=date_end)
        await postgres.subscribe(user_id=call.from_user.id, purse=purse)
        await postgres.update_sub_hairdresser(user_id=call.from_user.id, hairdresser='Да')
        services = await postgres.get_sub_master(user_id=call.from_user.id)
        await call.message.edit_text(text=f"В вашем кошельке: {purse} руб")
        await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
        await bot.send_message(chat_id=call.from_user.id,
                               text=f"Подписка успешно оформлена. Баланс вашего кошелька: {purse} руб")


@dp.callback_query_handler(text='hairdresser_no')
async def cancel_sub(call: types.CallbackQuery):
    services = await postgres.get_sub_master(user_id=call.from_user.id)
    await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))


@dp.callback_query_handler(text='visage-')
async def sub(call: types.CallbackQuery):
    purse_master = await postgres.purse(user_id=call.from_user.id)
    null = 0
    purse = int(purse_master[0]['purse']) - 100
    if purse < null:
        if await postgres.check_master_in_visage(user_id=call.from_user.id):
            check_date_subscription = await postgres.check_date_sub_visage(user_id=call.from_user.id)
            for check_date in check_date_subscription:
                if datetime.now() <= check_date['date_end']:
                    keyboard = types.InlineKeyboardMarkup(
                        inline_keyboard=[
                            [
                                InlineKeyboardButton(text=f'Подтвердить', callback_data=f'visage_yes:{purse}')
                            ],
                            [
                                InlineKeyboardButton(text=f'Отмена', callback_data=f'visage_no')
                            ]
                        ]
                    )
                    await call.message.edit_reply_markup(reply_markup=keyboard)

                else:
                    await bot.send_message(chat_id=call.from_user.id,
                                           text=f"Недостаточно средств. Баланс вашего кошелька: {purse_master[0]['purse']} руб")
        else:
            await bot.send_message(chat_id=call.from_user.id,
                                   text=f"Недостаточно средств. Баланс вашего кошелька: {purse_master[0]['purse']} руб")

    else:
        keyboard = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f'Подтвердить', callback_data=f'visage_yes:{purse}')
                ],
                [
                    InlineKeyboardButton(text=f'Отмена', callback_data=f'visage_no')
                ]
            ]
        )
        await call.message.edit_reply_markup(reply_markup=keyboard)


@dp.callback_query_handler(text_contains='visage_yes')
async def confirm(call: types.CallbackQuery):
    if await postgres.check_master_in_visage(user_id=call.from_user.id):
        check_date_subscription = await postgres.check_date_sub_visage(user_id=call.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_sub_visage(user_id=call.from_user.id, visage='Да')
                services = await postgres.get_sub_master(user_id=call.from_user.id)
                await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
                await bot.send_message(chat_id=call.from_user.id,
                                       text=f"Улуга активирована.")

            else:
                purse_back = call.data.split(":")[-1]
                purse = int(purse_back)
                date_start = datetime.now()
                date_end = date_start + timedelta(days=30)
                await postgres.subscribe(user_id=call.from_user.id, purse=purse)
                await postgres.update_sub_visage(user_id=call.from_user.id, visage='Да')
                await postgres.update_date_sub_visage(user_id=call.from_user.id, date_start=date_start,
                                                           date_end=date_end)
                services = await postgres.get_sub_master(user_id=call.from_user.id)
                await call.message.edit_text(text=f"В вашем кошельке: {purse} руб")
                await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
                await bot.send_message(chat_id=call.from_user.id,
                                       text=f"Подписка успешно оформлена. Баланс вашего кошелька: {purse} руб")

    else:
        purse_back = call.data.split(":")[-1]
        purse = int(purse_back)
        date_start = datetime.now()
        date_end = date_start + timedelta(days=30)
        makeup = 'Нет'
        eyebrows = 'Нет'
        eyelashes = 'Нет'
        wedding_image = 'Нет'
        await postgres.add_master_in_visage(user_id=call.from_user.id, makeup=makeup, eyelashes=eyelashes,
                                            eyebrows=eyebrows, wedding_image=wedding_image, date_start=date_start,
                                            date_end=date_end)
        await postgres.subscribe(user_id=call.from_user.id, purse=purse)
        await postgres.update_sub_visage(user_id=call.from_user.id, visage='Да')
        services = await postgres.get_sub_master(user_id=call.from_user.id)
        await call.message.edit_text(text=f"В вашем кошельке: {purse} руб")
        await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
        await bot.send_message(chat_id=call.from_user.id,
                               text=f"Подписка успешно оформлена. Баланс вашего кошелька: {purse} руб")


@dp.callback_query_handler(text='visage_no')
async def cancel_sub(call: types.CallbackQuery):
    services = await postgres.get_sub_master(user_id=call.from_user.id)
    await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))


@dp.callback_query_handler(text='other_services-')
async def sub(call: types.CallbackQuery):
    purse_master = await postgres.purse(user_id=call.from_user.id)
    purse = int(purse_master[0]['purse']) - 100
    null = 0
    if purse < null:
        if await postgres.check_master_in_other_services(user_id=call.from_user.id):
            check_date_subscription = await postgres.check_date_sub_other_services(user_id=call.from_user.id)
            for check_date in check_date_subscription:
                if datetime.now() <= check_date['date_end']:
                    keyboard = types.InlineKeyboardMarkup(
                        inline_keyboard=[
                            [
                                InlineKeyboardButton(text=f'Подтвердить', callback_data=f'other_services_yes:{purse}')
                            ],
                            [
                                InlineKeyboardButton(text=f'Отмена', callback_data=f'other_services_no')
                            ]
                        ]
                    )
                    await call.message.edit_reply_markup(reply_markup=keyboard)

                else:
                    await bot.send_message(chat_id=call.from_user.id,
                                           text=f"Недостаточно средств. Баланс вашего кошелька: {purse_master[0]['purse']} руб")
        else:
            await bot.send_message(chat_id=call.from_user.id,
                                   text=f"Недостаточно средств. Баланс вашего кошелька: {purse_master[0]['purse']} руб")

    else:
        keyboard = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f'Подтвердить', callback_data=f'other_services_yes:{purse}')
                ],
                [
                    InlineKeyboardButton(text=f'Отмена', callback_data=f'other_services_no')
                ]
            ]
        )
        await call.message.edit_reply_markup(reply_markup=keyboard)


@dp.callback_query_handler(text_contains='other_services_yes')
async def confirm(call: types.CallbackQuery):
    if await postgres.check_master_in_other_services(user_id=call.from_user.id):
        check_date_subscription = await postgres.check_date_sub_other_services(user_id=call.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_sub_other_services(user_id=call.from_user.id, other_services='Да')
                services = await postgres.get_sub_master(user_id=call.from_user.id)
                await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
                await bot.send_message(chat_id=call.from_user.id,
                                       text=f"Улуга активирована.")

            else:
                purse_back = call.data.split(":")[-1]
                purse = int(purse_back)
                date_start = datetime.now()
                date_end = date_start + timedelta(days=30)
                await postgres.subscribe(user_id=call.from_user.id, purse=purse)
                await postgres.update_sub_other_services(user_id=call.from_user.id, other_services='Да')
                await postgres.update_date_sub_other_services(user_id=call.from_user.id, date_start=date_start,
                                                              date_end=date_end)
                services = await postgres.get_sub_master(user_id=call.from_user.id)
                await call.message.edit_text(text=f"В вашем кошельке: {purse} руб")
                await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
                await bot.send_message(chat_id=call.from_user.id,
                                       text=f"Подписка успешно оформлена. Баланс вашего кошелька: {purse} руб")

    else:
        purse_back = call.data.split(":")[-1]
        purse = int(purse_back)
        date_start = datetime.now()
        date_end = date_start + timedelta(days=30)
        massage = 'Нет'
        depilation_with_wax = 'Нет'
        shugaring = 'Нет'
        tan_at_home = 'Нет'
        await postgres.add_master_in_other(user_id=call.from_user.id, massage=massage,
                                           depilation_with_wax=depilation_with_wax, shugaring=shugaring,
                                           date_start=date_start, date_end=date_end, tan_at_home=tan_at_home)
        await postgres.subscribe(user_id=call.from_user.id, purse=purse)
        await postgres.update_sub_other_services(user_id=call.from_user.id, other_services='Да')
        services = await postgres.get_sub_master(user_id=call.from_user.id)
        await call.message.edit_text(text=f"В вашем кошельке: {purse} руб")
        await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
        await bot.send_message(chat_id=call.from_user.id,
                               text=f"Подписка успешно оформлена. Баланс вашего кошелька: {purse} руб")


@dp.callback_query_handler(text='other_services_no')
async def cancel_sub(call: types.CallbackQuery):
    services = await postgres.get_sub_master(user_id=call.from_user.id)
    await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))


@dp.callback_query_handler(text='manicure+')
async def sub(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f'Подтвердить', callback_data=f'manicure_del')
            ],
            [
                InlineKeyboardButton(text=f'Отмена', callback_data=f'manicure_back')
            ]
        ]
    )
    await call.message.edit_reply_markup(reply_markup=keyboard)


@dp.callback_query_handler(text_contains='manicure_del')
async def confirm(call: types.CallbackQuery):
    if await postgres.check_master_in_manicure(user_id=call.from_user.id):
        check_date_subscription = await postgres.check_date_sub_manicure_pedicure(user_id=call.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_sub_manicure(user_id=call.from_user.id, manicure_pedicure='Нет')
                services = await postgres.get_sub_master(user_id=call.from_user.id)
                await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
                await bot.send_message(chat_id=call.from_user.id,
                                       text=f"Вы отменили услугу. Вы можете включить ее пока действует срок подписки")

            else:
                await postgres.update_sub_manicure(user_id=call.from_user.id, manicure_pedicure='Нет')
                services = await postgres.get_sub_master(user_id=call.from_user.id)
                await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
                await bot.send_message(chat_id=call.from_user.id,
                                       text=f"Вы отменили услугу.")


@dp.callback_query_handler(text='manicure_back')
async def cancel_sub(call: types.CallbackQuery):
    services = await postgres.get_sub_master(user_id=call.from_user.id)
    await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))


@dp.callback_query_handler(text='hairdresser+')
async def sub(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f'Подтвердить', callback_data=f'hairdresser_del')
            ],
            [
                InlineKeyboardButton(text=f'Отмена', callback_data=f'hairdresser_back')
            ]
        ]
    )
    await call.message.edit_reply_markup(reply_markup=keyboard)


@dp.callback_query_handler(text_contains='hairdresser_del')
async def confirm(call: types.CallbackQuery):
    if await postgres.check_master_in_hairdresser(user_id=call.from_user.id):
        check_date_subscription = await postgres.check_date_sub_hairdresser(user_id=call.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_sub_hairdresser(user_id=call.from_user.id, hairdresser='Нет')
                services = await postgres.get_sub_master(user_id=call.from_user.id)
                await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
                await bot.send_message(chat_id=call.from_user.id,
                                       text=f"Вы отменили услугу. Вы можете включить ее пока действует срок подписки")

            else:
                await postgres.update_sub_hairdresser(user_id=call.from_user.id, hairdresser='Нет')
                services = await postgres.get_sub_master(user_id=call.from_user.id)
                await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
                await bot.send_message(chat_id=call.from_user.id,
                                       text=f"Вы отменили услугу.")


@dp.callback_query_handler(text='hairdresser_back')
async def cancel_sub(call: types.CallbackQuery):
    services = await postgres.get_sub_master(user_id=call.from_user.id)
    await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))


@dp.callback_query_handler(text='visage+')
async def sub(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f'Подтвердить', callback_data=f'visage_del')
            ],
            [
                InlineKeyboardButton(text=f'Отмена', callback_data=f'visage_back')
            ]
        ]
    )
    await call.message.edit_reply_markup(reply_markup=keyboard)


@dp.callback_query_handler(text_contains='visage_del')
async def confirm(call: types.CallbackQuery):
    if await postgres.check_master_in_visage(user_id=call.from_user.id):
        check_date_subscription = await postgres.check_date_sub_visage(user_id=call.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_sub_visage(user_id=call.from_user.id, visage='Нет')
                services = await postgres.get_sub_master(user_id=call.from_user.id)
                await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
                await bot.send_message(chat_id=call.from_user.id,
                                       text=f"Вы отменили услугу. Вы можете включить ее пока действует срок подписки")

            else:
                await postgres.update_sub_visage(user_id=call.from_user.id, visage='Нет')
                services = await postgres.get_sub_master(user_id=call.from_user.id)
                await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
                await bot.send_message(chat_id=call.from_user.id,
                                       text=f"Вы отменили услугу.")


@dp.callback_query_handler(text='visage_back')
async def cancel_sub(call: types.CallbackQuery):
    services = await postgres.get_sub_master(user_id=call.from_user.id)
    await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))


@dp.callback_query_handler(text='other_services+')
async def sub(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f'Подтвердить', callback_data=f'other_services_del')
            ],
            [
                InlineKeyboardButton(text=f'Отмена', callback_data=f'other_services_back')
            ]
        ]
    )
    await call.message.edit_reply_markup(reply_markup=keyboard)


@dp.callback_query_handler(text_contains='other_services_del')
async def confirm(call: types.CallbackQuery):
    if await postgres.check_master_in_other_services(user_id=call.from_user.id):
        check_date_subscription = await postgres.check_date_sub_other_services(user_id=call.from_user.id)
        for check_date in check_date_subscription:
            if datetime.now() <= check_date['date_end']:
                await postgres.update_sub_other_services(user_id=call.from_user.id, other_services='Нет')
                services = await postgres.get_sub_master(user_id=call.from_user.id)
                await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
                await bot.send_message(chat_id=call.from_user.id,
                                       text=f"Вы отменили услугу. Вы можете включить ее пока действует срок подписки")

            else:
                await postgres.update_sub_other_services(user_id=call.from_user.id, other_services='Нет')
                services = await postgres.get_sub_master(user_id=call.from_user.id)
                await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))
                await bot.send_message(chat_id=call.from_user.id,
                                       text=f"Вы отменили услугу.")


@dp.callback_query_handler(text='other_services_back')
async def cancel_sub(call: types.CallbackQuery):
    services = await postgres.get_sub_master(user_id=call.from_user.id)
    await call.message.edit_reply_markup(reply_markup=sub_keyboard(services))


@dp.callback_query_handler(text='back')
async def sub(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='💳 Пополнить кошелек', callback_data='replenish')
            ],
            [
                InlineKeyboardButton(text='📝 Управление подпиской', callback_data='subscription')
            ],
            [
                InlineKeyboardButton(text='💶 Донат', callback_data='donation')
            ]
        ]
    )
    await call.message.edit_reply_markup(reply_markup=keyboard)


