from aiogram import types
from aiogram.types import InlineKeyboardButton

from data.prolong_sub import prolong_sub
from filters import CheckUsers, CheckMaster, CheckClient, CheckMasterCall, CheckClientCall
from loader import dp, bot
from utils.db_api import postgres


@dp.message_handler(CheckMaster(), text='🏅 Найти мастера по рейтингу')
async def like(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Топ 25 мастеров', callback_data='top'),
                InlineKeyboardButton(text='Мой рейтинг', callback_data='rating_master')
            ],
            [
                InlineKeyboardButton(text='🔎 Поиск мастера', callback_data='find_master')
            ],
            [
                InlineKeyboardButton(text='🏅 Оставить отзыв мастеру', callback_data='feedback_master')
            ],
            [
                InlineKeyboardButton(text='🏅 Оставить отзыв клиенту', callback_data='feedback_client')
            ]
        ]
    )
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Здесь Вы можете найти мастера, оценить мастера или клиента, а также узнать свой рейтинг и 25 лучших мастеров",
                           reply_markup=keyboard)


@dp.message_handler(CheckClient(), text='🏅 Найти мастера по рейтингу')
async def like(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Топ 25 мастеров', callback_data='top'),
                InlineKeyboardButton(text='Мой рейтинг', callback_data='rating_client')
            ],
            [
                InlineKeyboardButton(text='🔎 Поиск мастера', callback_data='find_master')
            ],
            [
                InlineKeyboardButton(text='🏅 Оставить отзыв мастеру', callback_data='feedback_master')
            ]
        ]
    )
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Здесь Вы можете найти мастера, оценить мастера, а также узнать свой рейтинг и 25 лучших мастеров",
                           reply_markup=keyboard)


@dp.callback_query_handler(text='find_master')
async def cancel_sub(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🔎 Искать по ID пользователя', switch_inline_query_current_chat='№:')
            ],
            [
                InlineKeyboardButton(text='🔎 Искать по имени', switch_inline_query_current_chat='Никнейм:')
            ],
            [
                InlineKeyboardButton(text='⬅️ Назад', callback_data='back_find')
            ]

        ]
    )
    await call.message.edit_reply_markup(reply_markup=keyboard)


@dp.callback_query_handler(CheckMasterCall(), text='back_find')
async def cancel_sub(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Топ 25 мастеров', callback_data='top'),
                InlineKeyboardButton(text='Мой рейтинг', callback_data='rating_master')
            ],
            [
                InlineKeyboardButton(text='🔎 Поиск мастера', callback_data='find_master')
            ],
            [
                InlineKeyboardButton(text='🏅 Оставить отзыв мастеру', callback_data='feedback_master')
            ],
            [
                InlineKeyboardButton(text='🏅 Оставить отзыв клиенту', callback_data='feedback_client')
            ]
        ]
    )
    await call.message.edit_text(text='Здесь Вы можете найти мастера, оценить мастера или клиента, а также узнать свой рейтинг и 25 лучших мастеров')
    await call.message.edit_reply_markup(reply_markup=keyboard)


@dp.callback_query_handler(CheckClientCall(), text='back_find')
async def cancel_sub(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Топ 25 мастеров', callback_data='top'),
                InlineKeyboardButton(text='Мой рейтинг', callback_data='rating_client')
            ],
            [
                InlineKeyboardButton(text='🔎 Поиск мастера', callback_data='find_master')
            ],
            [
                InlineKeyboardButton(text='🏅 Оставить отзыв мастеру', callback_data='feedback_master')
            ]
        ]
    )
    await call.message.edit_text(text='Здесь Вы можете найти мастера, оценить мастера, а также узнать свой рейтинг и 25 лучших мастеров')
    await call.message.edit_reply_markup(reply_markup=keyboard)
