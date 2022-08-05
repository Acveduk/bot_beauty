from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputFile

from data.profile import find_master, services_master
from data.prolong_sub import prolong_sub
from filters import CheckUsers
from loader import dp, bot
from utils.db_api import postgres


@dp.message_handler(CheckUsers(), text='❤️Избранное')
async def favorites(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранные мастера')
    keyboard.row('🏆 Активные заявки')
    keyboard.row('⬅️ назад')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Здесь Вы можете посмотреть профиль мастеров которых вы добавили в избраное, и свои активные заявки',
                           reply_markup=keyboard)


@dp.message_handler(CheckUsers(), text='❤️Избранные мастера')
async def favorites_master(message: types.Message):
    if await postgres.check_user_in_favorites(user_id=message.from_user.id):
        favorite = await postgres.select_master_in_favorites(user_id=message.from_user.id)
        i = await postgres.get_user(user_id=message.from_user.id)
        for favorite_master in favorite:
            master = await postgres.get_user(user_id=favorite_master['master_id'])
            services = await services_master(user_id=favorite_master['master_id'])
            if await postgres.check_rating_master(user_id=master[0]['user_id']):
                rating = await postgres.select_rating_master(user_id=master[0]['user_id'])
                await bot.send_photo(chat_id=message.from_user.id,
                                     photo=f"{master[0]['photo']}",
                                     caption=find_master(master=master, rating=rating, services=services),
                                     reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                       inline_keyboard=[
                                                                           [
                                                                               InlineKeyboardButton(
                                                                                   text="Написать мастеру",
                                                                                   url=f"tg://user?id={master[0]['user_id']}"
                                                                               )
                                                                           ],
                                                                           [
                                                                               InlineKeyboardButton(
                                                                                   text="Удалить из избранного",
                                                                                   callback_data=f"delete:{master[0]['user_id']}"
                                                                               )
                                                                           ]
                                                                       ])
                                     )
                if await postgres.check_master_in_recall(user_id=master[0]['user_id']):
                    await bot.send_document(chat_id=message.from_user.id,
                                            document=InputFile(f"feedback_master/{master[0]['user_id']}.txt"),
                                            caption='Все отзывы о мастере')
                else:
                    await bot.send_message(chat_id=message.from_user.id,
                                           text='Отзывов о клиенте еще нет\n'
                                                'Будьте первым 😉')
            else:
                rating = 0
                await bot.send_photo(chat_id=message.from_user.id,
                                     photo=f"{master[0]['photo']}",
                                     caption=find_master(master=master, rating=rating, services=services),
                                     reply_markup=InlineKeyboardMarkup(row_width=1,
                                                                       inline_keyboard=[
                                                                           [
                                                                               InlineKeyboardButton(
                                                                                   text="Написать мастеру",
                                                                                   url=f"tg://user?id={master[0]['user_id']}"
                                                                               )
                                                                           ],
                                                                           [
                                                                               InlineKeyboardButton(
                                                                                   text="Удалить из избранного",
                                                                                   callback_data=f"delete:{master[0]['user_id']}"
                                                                               )
                                                                           ]
                                                                       ]))
                if await postgres.check_master_in_recall(user_id=master[0]['user_id']):
                    await bot.send_document(chat_id=message.from_user.id,
                                            document=InputFile(f"feedback_master/{master[0]['user_id']}.txt"),
                                            caption='Все отзывы о мастере')
                else:
                    await bot.send_message(chat_id=message.from_user.id,
                                           text='Отзывов о мастере еще нет\n'
                                                'Будьте первым 😉')

    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text='У вас нет избранных мастеров :(\n')


@dp.callback_query_handler(text_contains='delete')
async def profile(call: types.CallbackQuery):
    master_id = call.data.split(":")[-1]
    master_id = int(master_id)
    await postgres.delete_master_in_favorites(user_id=call.from_user.id, master_id=master_id)
    await bot.send_message(chat_id=call.from_user.id,
                           text='Вы успешно удалили мастера из избранного 💔')


@dp.message_handler(CheckUsers(), text='🏆 Активные заявки')
async def app(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    application = await postgres.select_number_applications_favorites(user_id=message.from_user.id)
    text = ''
    c = 0
    for app in application:
        c += 1
        text += f"{c}. #з{app['number_applications']}: {app['service']}\n\n"

    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Ваши последнии 5 заявок:\n\n'
                                f'{text}')