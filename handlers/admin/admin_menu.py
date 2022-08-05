from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputFile

from data.profile import services_master, profile_user
from filters import CheckAdmin
from loader import dp, bot
from states.state_users import Find_user
from utils.db_api import postgres


@dp.message_handler(CheckAdmin(), text='👨‍💻 Админ')
async def admin_menu(message: types.Message):
    if await postgres.check_admin_in_database(admin_id=message.from_user.id):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('👥 Кол-во пользователей')
        keyboard.row('📱 Найти пользователя')
        keyboard.row('✍️Написать пользователям')
        keyboard.row('⬅️ назад')

        await bot.send_message(chat_id=message.from_user.id,
                               text='Добро пожаловать в меню администратора',
                               reply_markup=keyboard)


@dp.message_handler(CheckAdmin(), text='📱 Найти пользователя')
async def find_users(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🔎 Искать по ID пользователя', switch_inline_query_current_chat='№:')
            ],
            [
                InlineKeyboardButton(text='🔎 Искать по имени', switch_inline_query_current_chat='Никнейм:')
            ],
            [
                InlineKeyboardButton(text='🔎 Искать по номеру телефону', switch_inline_query_current_chat='Телефон:')
            ]

        ]
    )
    await message.answer(f'Вы можете найти пользователя в inline режиме',
                         reply_markup=keyboard)


@dp.inline_handler(CheckAdmin())
async def users_find(query: types.InlineQuery):
    results = []
    clients = await postgres.select_all_user_user_number(text=query.query)
    for user in clients:
        results.append(types.InlineQueryResultArticle(
            id=str(user['user_number']),
            title=user['name_user'],
            input_message_content=types.InputTextMessageContent(
                message_text=f"Мастер: {user['name_user']}"
            ),
            description=f"Номер мастера: {user['user_number']}\n"
                        f"Номер телефона: {user['phone_number']}",
            reply_markup=InlineKeyboardMarkup(row_width=1,
                                              inline_keyboard=[
                                                  [
                                                      InlineKeyboardButton(
                                                          text="👤 Посмотреть профиль",
                                                          callback_data=f"admin:{user['user_id']}"
                                                      )
                                                  ]
                                              ])
        )
        )

    await query.answer(cache_time=5, results=results)


@dp.callback_query_handler(text_contains='admin')
async def profile(call: types.CallbackQuery):
    user_id = call.data.split(":")[-1]
    user_id = int(user_id)
    master = await postgres.get_user(user_id=user_id)
    services = await services_master(user_id=user_id)

    if await postgres.check_ban(user_id=user_id):
        if await postgres.check_rating_master(user_id=user_id):
            rating = await postgres.select_rating_master(user_id=user_id)
            await bot.send_photo(chat_id=call.from_user.id,
                                 photo=f"{master[0]['photo']}",
                                 caption=profile_user(user=master, rating=rating, services=services),
                                 reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                   inline_keyboard=[
                                                                       [
                                                                           InlineKeyboardButton(
                                                                               text="Написать",
                                                                               callback_data=f"write:{user_id}"
                                                                           )
                                                                       ],
                                                                       [
                                                                           InlineKeyboardButton(
                                                                               text="Удалить",
                                                                               callback_data=f"out:{user_id}"
                                                                           )
                                                                       ],
                                                                       [
                                                                           InlineKeyboardButton(
                                                                               text="Разбанить",
                                                                               callback_data=f"unblock:{user_id}"
                                                                           )
                                                                       ]
                                                                   ])
                                 )
            if await postgres.check_master_in_recall(user_id=user_id):
                await bot.send_document(chat_id=call.from_user.id,
                                        document=InputFile(f"feedback_master/{user_id}.txt"),
                                        caption='Все отзывы о мастере')

            else:
                await bot.send_message(chat_id=call.from_user.id,
                                       text='Отзывов о мастере еще нет\n'
                                            'Будьте первым 😉')

        elif await postgres.check_rating_client(user_id=user_id):
            rating = await postgres.select_rating_client(user_id=user_id)
            await bot.send_photo(chat_id=call.from_user.id,
                                 photo=f"{master[0]['photo']}",
                                 caption=profile_user(user=master, rating=rating, services=services),
                                 reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                   inline_keyboard=[
                                                                       [
                                                                           InlineKeyboardButton(
                                                                               text="Написать",
                                                                               callback_data=f"write:{user_id}"
                                                                           )
                                                                       ],
                                                                       [
                                                                           InlineKeyboardButton(
                                                                               text="Удалить",
                                                                               callback_data=f"out:{user_id}"
                                                                           )
                                                                       ],
                                                                       [
                                                                           InlineKeyboardButton(
                                                                               text="Разбанить",
                                                                               callback_data=f"unblock:{user_id}"
                                                                           )
                                                                       ]
                                                                   ])
                                 )
            if await postgres.check_recall_client(user_id=user_id):
                await bot.send_document(chat_id=call.from_user.id,
                                        document=InputFile(f"feedback_client/{user_id}.txt"),
                                        caption='Все отзывы о мастере')

            else:
                await bot.send_message(chat_id=call.from_user.id,
                                       text='Отзывов о клиенте еще нет\n'
                                            'Будьте первым 😉')

        else:
            rating = 0
            await bot.send_photo(chat_id=call.from_user.id,
                                 photo=f"{master[0]['photo']}",
                                 caption=profile_user(user=master, rating=rating, services=services),
                                 reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                   inline_keyboard=[
                                                                       [
                                                                           InlineKeyboardButton(
                                                                               text="Написать",
                                                                               callback_data=f"write:{user_id}"
                                                                           )
                                                                       ],
                                                                       [
                                                                           InlineKeyboardButton(
                                                                               text="Удалить",
                                                                               callback_data=f"out:{user_id}"
                                                                           )
                                                                       ],
                                                                       [
                                                                           InlineKeyboardButton(
                                                                               text="Разбанить",
                                                                               callback_data=f"unblock:{user_id}"
                                                                           )
                                                                       ]
                                                                   ]))
            if await postgres.check_master_in_recall(user_id=user_id):
                await bot.send_document(chat_id=call.from_user.id,
                                        document=InputFile(f"feedback_master/{user_id}.txt"),
                                        caption='Все отзывы о мастере')

            elif await postgres.check_recall_client(user_id=user_id):
                await bot.send_document(chat_id=call.from_user.id,
                                        document=InputFile(f"feedback_client/{user_id}.txt"),
                                        caption='Все отзывы о мастере')

            else:
                await bot.send_message(chat_id=call.from_user.id,
                                       text='Отзывов о пользователе еще нет\n'
                                            'Будьте первым 😉')
    else:
        if await postgres.check_rating_master(user_id=user_id):
            rating = await postgres.select_rating_master(user_id=user_id)
            await bot.send_photo(chat_id=call.from_user.id,
                                 photo=f"{master[0]['photo']}",
                                 caption=profile_user(user=master, rating=rating, services=services),
                                 reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                   inline_keyboard=[
                                                                       [
                                                                           InlineKeyboardButton(
                                                                               text="Написать",
                                                                               callback_data=f"write:{user_id}"
                                                                           )
                                                                       ],
                                                                       [
                                                                           InlineKeyboardButton(
                                                                               text="Удалить",
                                                                               callback_data=f"out:{user_id}"
                                                                           )
                                                                       ],
                                                                       [
                                                                           InlineKeyboardButton(
                                                                               text="Забанить",
                                                                               callback_data=f"ban:{user_id}"
                                                                           )
                                                                       ]
                                                                   ])
                                 )
            if await postgres.check_master_in_recall(user_id=user_id):
                await bot.send_document(chat_id=call.from_user.id,
                                        document=InputFile(f"feedback_master/{user_id}.txt"),
                                        caption='Все отзывы о мастере')

            else:
                await bot.send_message(chat_id=call.from_user.id,
                                       text='Отзывов о мастере еще нет\n'
                                            'Будьте первым 😉')

        elif await postgres.check_rating_client(user_id=user_id):
            rating = await postgres.select_rating_client(user_id=user_id)
            await bot.send_photo(chat_id=call.from_user.id,
                                 photo=f"{master[0]['photo']}",
                                 caption=profile_user(user=master, rating=rating, services=services),
                                 reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                   inline_keyboard=[
                                                                       [
                                                                           InlineKeyboardButton(
                                                                               text="Написать",
                                                                               callback_data=f"write:{user_id}"
                                                                           )
                                                                       ],
                                                                       [
                                                                           InlineKeyboardButton(
                                                                               text="Удалить",
                                                                               callback_data=f"out:{user_id}"
                                                                           )
                                                                       ],
                                                                       [
                                                                           InlineKeyboardButton(
                                                                               text="Забанить",
                                                                               callback_data=f"ban:{user_id}"
                                                                           )
                                                                       ]
                                                                   ])
                                 )
            if await postgres.check_recall_client(user_id=user_id):
                await bot.send_document(chat_id=call.from_user.id,
                                        document=InputFile(f"feedback_client/{user_id}.txt"),
                                        caption='Все отзывы о мастере')

            else:
                await bot.send_message(chat_id=call.from_user.id,
                                       text='Отзывов о клиенте еще нет\n'
                                            'Будьте первым 😉')

        else:
            rating = 0
            await bot.send_photo(chat_id=call.from_user.id,
                                 photo=f"{master[0]['photo']}",
                                 caption=profile_user(user=master, rating=rating, services=services),
                                 reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                   inline_keyboard=[
                                                                       [
                                                                           InlineKeyboardButton(
                                                                               text="Написать",
                                                                               callback_data=f"write:{user_id}"
                                                                           )
                                                                       ],
                                                                       [
                                                                           InlineKeyboardButton(
                                                                               text="Удалить",
                                                                               callback_data=f"out:{user_id}"
                                                                           )
                                                                       ],
                                                                       [
                                                                           InlineKeyboardButton(
                                                                               text="Забанить",
                                                                               callback_data=f"ban:{user_id}"
                                                                           )
                                                                       ]
                                                                   ]))
            if await postgres.check_master_in_recall(user_id=user_id):
                await bot.send_document(chat_id=call.from_user.id,
                                        document=InputFile(f"feedback_master/{user_id}.txt"),
                                        caption='Все отзывы о мастере')

            elif await postgres.check_recall_client(user_id=user_id):
                await bot.send_document(chat_id=call.from_user.id,
                                        document=InputFile(f"feedback_client/{user_id}.txt"),
                                        caption='Все отзывы о мастере')

            else:
                await bot.send_message(chat_id=call.from_user.id,
                                       text='Отзывов о пользователе еще нет\n'
                                            'Будьте первым 😉')


@dp.callback_query_handler(text_contains="write")
async def write_user(call: types.CallbackQuery, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ назад')
    user_id = int(call.data.split(":")[-1])
    await state.update_data(user_id=user_id)
    await bot.send_message(chat_id=call.from_user.id, text='Введите сообщение пользователю', reply_markup=keyboard)

    await Find_user.user_id.set()


@dp.message_handler(text='⬅️ назад', state=Find_user.user_id)
async def channel(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('👥 Кол-во пользователей')
    keyboard.row('📱 Найти пользователя')
    keyboard.row('✍️Написать пользователям')
    keyboard.row('⬅️ назад')
    await bot.send_message(chat_id=message.from_user.id, text='Добро пожаловать в меню администратора',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(state=Find_user.user_id)
async def answer_admin(message: types.Message, state: FSMContext):
    admin_message = message.text
    data = await state.get_data()
    user_id = data.get("user_id")
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Сообщение доставлено')
    await bot.send_message(chat_id=user_id,
                           text=f'Вам написал администратор: {message.from_user.full_name}'
                                f'\n'
                                f'Сообщение: {admin_message}')

    await state.finish()


@dp.callback_query_handler(text_contains="out")
async def delete_user(call: types.CallbackQuery):
    user_id = int(call.data.split(":")[-1])
    await postgres.delete_user(user_id=user_id)

    await bot.send_message(chat_id=call.from_user.id,
                           text='Вы успешно удалили пользователя')


@dp.callback_query_handler(text_contains="unblock")
async def delete_user(call: types.CallbackQuery):
    user_id = int(call.data.split(":")[-1])
    await postgres.unblock_user(user_id=user_id)

    await bot.send_message(chat_id=call.from_user.id,
                           text='Вы успешно разбанили пользователя')

@dp.callback_query_handler(text_contains="ban")
async def delete_user(call: types.CallbackQuery):
    user_id = int(call.data.split(":")[-1])
    await postgres.ban_user(user_id=user_id)

    await bot.send_message(chat_id=call.from_user.id,
                           text='Вы успешно забанили пользователя')