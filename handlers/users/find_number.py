from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputFile

from data.profile import profile_user, services_master, find_master
from loader import dp, bot
from utils.db_api import postgres


@dp.inline_handler()
async def users_find(query: types.InlineQuery):
    results = []
    clients = await postgres.select_all_client_user_number(text=query.query)
    for user in clients:
        results.append(types.InlineQueryResultArticle(
            id=str(user['user_number']),
            title=user['name_user'],
            input_message_content=types.InputTextMessageContent(
                message_text=f"Мастер: {user['name_user']}"
            ),
            description=f"Номер мастера: {user['user_number']}\n",
            reply_markup=InlineKeyboardMarkup(row_width=1,
                                              inline_keyboard=[
                                                  [
                                                      InlineKeyboardButton(
                                                          text="👤 Посмотреть профиль",
                                                          callback_data=f"profile:{user['user_id']}"
                                                      )
                                                  ]
                                              ])
        )
        )

    await query.answer(cache_time=5, results=results)


@dp.callback_query_handler(text_contains='profile')
async def profile(call: types.CallbackQuery):
    user_id = call.data.split(":")[-1]
    user_id = int(user_id)
    master = await postgres.get_user(user_id=user_id)
    services = await services_master(user_id=user_id)

    if await postgres.check_rating_master(user_id=user_id):
        rating = await postgres.select_rating_master(user_id=user_id)
        await bot.send_photo(chat_id=call.from_user.id,
                             photo=f"{master[0]['photo']}",
                             caption=find_master(master=master, rating=rating, services=services),
                             reply_markup=InlineKeyboardMarkup(row_width=1,
                                                               inline_keyboard=[
                                                                   [
                                                                       InlineKeyboardButton(
                                                                           text="Написать мастеру",
                                                                           url=f"tg://user?id={user_id}"
                                                                       )
                                                                   ],
                                                                   [
                                                                       InlineKeyboardButton(
                                                                           text="Добавить в избранное",
                                                                           callback_data=f"favorite:{user_id}"
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
                                   text='Отзывов о клиенте еще нет\n'
                                        'Будьте первым 😉')
    else:
        rating = 0
        await bot.send_photo(chat_id=call.from_user.id,
                             photo=f"{master[0]['photo']}",
                             caption=find_master(master=master, rating=rating, services=services),
                             reply_markup=InlineKeyboardMarkup(row_width=1,
                                                               inline_keyboard=[
                                                                   [
                                                                       InlineKeyboardButton(
                                                                           text="Написать мастеру",
                                                                           url=f"tg://user?id={user_id}"
                                                                       )
                                                                   ],
                                                                   [
                                                                       InlineKeyboardButton(
                                                                           text="Добавить в избранное",
                                                                           callback_data=f"favorite:{user_id}"
                                                                       )
                                                                   ]
                                                               ]))
        if await postgres.check_master_in_recall(user_id=user_id):
            await bot.send_document(chat_id=call.from_user.id,
                                    document=InputFile(f"feedback_master/{user_id}.txt"),
                                    caption='Все отзывы о мастере')
        else:
            await bot.send_message(chat_id=call.from_user.id,
                                   text='Отзывов о мастере еще нет\n'
                                        'Будьте первым 😉')


@dp.callback_query_handler(text_contains='favorite')
async def profile(call: types.CallbackQuery):
    master_id = call.data.split(":")[-1]
    master_id = int(master_id)
    await postgres.add_master_in_favorites(user_id=call.from_user.id, master_id=master_id)
    await bot.send_message(chat_id=call.from_user.id,
                           text='Вы успешно добавили мастера в избранное ❤️')
