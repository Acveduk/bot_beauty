from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton

from loader import dp, bot
from states.state_users import Feedback_master
from utils.db_api import postgres


@dp.callback_query_handler(text_contains='feedback_master')
async def feedback(call: types.CallbackQuery, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('Отмена')
    await bot.send_message(chat_id=call.from_user.id, text=f"Введите ID мастера:\n"
                                                           f"Например: ID:1", reply_markup=keyboard)
    await Feedback_master.master.set()


@dp.message_handler(text='Отмена', state=Feedback_master.master)
async def feedback(call: types.CallbackQuery, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')
    await bot.send_message(chat_id=call.from_user.id, text=f"Вы вернулись в главное меню", reply_markup=keyboard)
    await state.finish()


@dp.message_handler(state=Feedback_master.master)
async def feedback(message: types.Message, state: FSMContext):
    id_user = message.text.split(":")[-1]
    id_user = int(id_user)
    master = await postgres.get_master(user_number=id_user)
    if master != []:
        if master[0]['manicure_pedicure'] and master[0]['hairdresser'] and master[0]['visage'] and master[0]['other_services'] == 'Пусто':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.row('Отмена')
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Пользователь не является мастером.\n\n"
                                        f"Введите ID мастера:\n"
                                        f"Например: ID:1",
                                   reply_markup=keyboard)
            await Feedback_master.master.set()

        else:
            user_id = int(master[0]['user_id'])
            keyboard = types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(text='➖', callback_data='one_star'),
                        InlineKeyboardButton(text='➖', callback_data='two_star'),
                        InlineKeyboardButton(text='➖', callback_data='three_star'),
                        InlineKeyboardButton(text='➖', callback_data='four_star'),
                        InlineKeyboardButton(text='➖', callback_data='five_star')
                    ]
                ]
            )
            keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard2.row('Отмена')
            await state.update_data(user_id=user_id)
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"Подготовка поля отзыва о мастере: {master[0]['name_user']}",
                                   reply_markup=keyboard2)
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"1/3. Поставьте звезды пользователю",
                                   reply_markup=keyboard)
            await Feedback_master.star.set()
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('Отмена')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Пользователь c таким ID нет в базе данных, либо он удален.\n\n"
                                    f"Введите ID мастера:\n"
                                    f"Например: ID:1",
                               reply_markup=keyboard)
        await Feedback_master.master.set()


@dp.message_handler(text='Отмена', state=Feedback_master.star)
async def feedback(call: types.CallbackQuery, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')
    await bot.send_message(chat_id=call.from_user.id, text=f"Вы вернулись в главное меню", reply_markup=keyboard)
    await state.finish()


@dp.callback_query_handler(text=['one_star', 'two_star', 'three_star', 'four_star', 'five_star'], state=[Feedback_master.star, Feedback_master.feedback])
async def feedback(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'one_star':
        keyboard = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='⭐️', callback_data='one_star'),
                    InlineKeyboardButton(text='➖', callback_data='two_star'),
                    InlineKeyboardButton(text='➖', callback_data='three_star'),
                    InlineKeyboardButton(text='➖', callback_data='four_star'),
                    InlineKeyboardButton(text='➖', callback_data='five_star')
                ],
                [
                    InlineKeyboardButton(text='Подтвердить', callback_data='сonfirm')
                ]
            ]
        )
        star = 1
        await state.update_data(star=star)
        await call.message.edit_text(text='2/3. Нажмите "подтвердить" для сохранения оценки')
        await call.message.edit_reply_markup(reply_markup=keyboard)
        await Feedback_master.feedback.set()

    elif call.data == 'two_star':
        keyboard = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='⭐️', callback_data='one_star'),
                    InlineKeyboardButton(text='⭐️', callback_data='two_star'),
                    InlineKeyboardButton(text='➖', callback_data='three_star'),
                    InlineKeyboardButton(text='➖', callback_data='four_star'),
                    InlineKeyboardButton(text='➖', callback_data='five_star')
                ],
                [
                    InlineKeyboardButton(text='Подтвердить', callback_data='сonfirm')
                ]
            ]
        )
        star = 2
        await state.update_data(star=star)
        await call.message.edit_text(text='2/3. Нажмите "подтвердить" для сохранения оценки')
        await call.message.edit_reply_markup(reply_markup=keyboard)
        await Feedback_master.feedback.set()

    elif call.data == 'three_star':
        keyboard = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='⭐️', callback_data='one_star'),
                    InlineKeyboardButton(text='⭐️', callback_data='two_star'),
                    InlineKeyboardButton(text='⭐️', callback_data='three_star'),
                    InlineKeyboardButton(text='➖', callback_data='four_star'),
                    InlineKeyboardButton(text='➖', callback_data='five_star')
                ],
                [
                    InlineKeyboardButton(text='Подтвердить', callback_data='сonfirm')
                ]
            ]
        )
        star = 3
        await state.update_data(star=star)
        await call.message.edit_text(text='2/3. Нажмите "подтвердить" для сохранения оценки')
        await call.message.edit_reply_markup(reply_markup=keyboard)
        await Feedback_master.feedback.set()

    elif call.data == 'four_star':
        keyboard = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='⭐️', callback_data='one_star'),
                    InlineKeyboardButton(text='⭐️', callback_data='two_star'),
                    InlineKeyboardButton(text='⭐️', callback_data='three_star'),
                    InlineKeyboardButton(text='⭐️', callback_data='four_star'),
                    InlineKeyboardButton(text='➖', callback_data='five_star')
                ],
                [
                    InlineKeyboardButton(text='Подтвердить', callback_data='сonfirm')
                ]
            ]
        )
        star = 4
        await state.update_data(star=star)
        await call.message.edit_text(text='2/3. Нажмите "подтвердить" для сохранения оценки')
        await call.message.edit_reply_markup(reply_markup=keyboard)
        await Feedback_master.feedback.set()

    elif call.data == 'five_star':
        keyboard = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='⭐️', callback_data='one_star'),
                    InlineKeyboardButton(text='⭐️', callback_data='two_star'),
                    InlineKeyboardButton(text='⭐️', callback_data='three_star'),
                    InlineKeyboardButton(text='⭐️', callback_data='four_star'),
                    InlineKeyboardButton(text='⭐️', callback_data='five_star')
                ],
                [
                    InlineKeyboardButton(text='Подтвердить', callback_data='сonfirm')
                ]
            ]
        )
        star = 5
        await state.update_data(star=star)
        await call.message.edit_text(text='2/3. Нажмите "подтвердить" для сохранения оценки')
        await call.message.edit_reply_markup(reply_markup=keyboard)
        await Feedback_master.feedback.set()


@dp.callback_query_handler(text='сonfirm', state=Feedback_master.feedback)
async def feedback(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    star = data.get("star")
    user_id = data.get('user_id')
    await postgres.add_rating_master(user_id=user_id, client_id=call.from_user.id, rating=star)
    await call.message.edit_reply_markup()
    await call.message.edit_text(text='3/3. Напишите отзыв мастеру')
    await Feedback_master.recall.set()


@dp.message_handler(text='Отмена', state=Feedback_master.feedback)
async def feedback(call: types.CallbackQuery, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')
    await bot.send_message(chat_id=call.from_user.id, text=f"Вы вернулись в главное меню", reply_markup=keyboard)
    await state.finish()

@dp.message_handler(text='Отмена', state=Feedback_master.recall)
async def feedback(call: types.CallbackQuery, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')
    await bot.send_message(chat_id=call.from_user.id, text=f"Вы вернулись в главное меню", reply_markup=keyboard)
    await state.finish()


@dp.message_handler(state=Feedback_master.recall)
async def feedback_client(message: types.Message, state: FSMContext):
    recall = message.text
    data = await state.get_data()
    user_id = data.get("user_id")
    name_recall = message.from_user.full_name
    if await postgres.check_recall_master(user_id=user_id):
        await postgres.add_recall_master(user_id=user_id, recall=recall, name_recall=name_recall)
        with open(f'feedback_master/{user_id}.txt', 'a', encoding='utf-8') as file:
            file.write(f'Отзыв оставил(а): {name_recall}\n'
                       f'Отзыв: {recall}\n\n')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
        keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
        keyboard.row('💰 Кошелек', '📂 Мой профиль')
        keyboard.row('ℹ️Как работать с ботом')
        await bot.send_message(chat_id=message.from_user.id, text='Вы успешно оставили отзыв мастеру', reply_markup=keyboard)
        await state.finish()



    else:
        await postgres.add_recall_master(user_id=user_id, recall=recall, name_recall=name_recall)
        with open(f'feedback_master/{user_id}.txt', 'w', encoding='utf-8') as file:
            file.write(f'Отзыв оставил(а): {name_recall}\n'
                       f'Отзыв: {recall}\n\n')

        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
        keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
        keyboard.row('💰 Кошелек', '📂 Мой профиль')
        keyboard.row('ℹ️Как работать с ботом')
        await bot.send_message(chat_id=message.from_user.id, text='Вы успешно оставили отзыв мастеру', reply_markup=keyboard)
        await state.finish()
