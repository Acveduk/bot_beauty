from aiogram import types
from aiogram.types import InlineKeyboardButton

from data.prolong_sub import prolong_sub
from filters import CheckUsers, CheckClient, CheckMaster
from loader import dp, bot
from utils.db_api import postgres


@dp.message_handler(CheckClient(), text='💬 Канал/Чат')
async def bot_start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='💭 Чат', url='https://t.me/poiskmasterachat'),
                InlineKeyboardButton(text='🗣 Канал', url='https://t.me/poisk_mastera')
            ]
        ]
    )
    await bot.send_message(chat_id=message.from_user.id,
                           text='Перейдите в наш канал или чат',
                           reply_markup=keyboard)

@dp.message_handler(CheckMaster(), text='💬 Канал/Чат')
async def bot_start(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='💭 Чат', url='https://t.me/poiskmasterachat'),
                InlineKeyboardButton(text='🗣 Канал', url='https://t.me/poisk_mastera')
            ],
            [
                InlineKeyboardButton(text='🤖 Бот для мастера', url='https://t.me/poiskbeautimasterabot')
            ]
        ]
    )
    await bot.send_message(chat_id=message.from_user.id,
                           text='Перейдите в наш канал или чат',
                           reply_markup=keyboard)