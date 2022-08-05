from aiogram import types
from aiogram.dispatcher import FSMContext

from data.prolong_sub import prolong_sub
from filters import CheckUsers
from loader import dp, bot
from states.state_users import Echo


@dp.message_handler(CheckUsers())
async def echo(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    user_message = message.text
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(text='Перенаправить в бота', callback_data=f"echo:{message.from_user.id}"))
    await bot.send_message(chat_id='@testchannalmy',
                           text=f'Пользователь: {message.from_user.full_name}\n'
                                f'Пишет в бота не используя команды: {user_message}',
                           reply_markup=keyboard)
    await bot.send_message(chat_id=message.from_user.id,
                           text='Используйте кнопки ниже')


@dp.callback_query_handler(text_contains="echo")
async def cancel_payment(call: types.CallbackQuery,):
    user_id = call.data.split(":")[-1]
    user_id = int(user_id)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Ответить', callback_data=f"info:{user_id}"))

    keyboard2 = types.InlineKeyboardMarkup()
    keyboard2.add(types.InlineKeyboardButton(text='Перейти в бота', url=f"https://t.me/hheellooworld_bot"))
    await call.message.edit_reply_markup(reply_markup=keyboard2)
    await bot.send_message(chat_id=call.from_user.id,
                           text='Нажмите на кнопку, чтобы ответить пользователю',
                           reply_markup=keyboard)


@dp.callback_query_handler(text_contains="info")
async def cancel_payment(call: types.CallbackQuery, state: FSMContext):
    user_id = call.data.split(":")[-1]
    user_id = int(user_id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ назад')
    await state.update_data(user_id=user_id)
    await bot.send_message(chat_id=call.from_user.id,
                           text='Введите ответ пользователю',
                           reply_markup=keyboard)
    await Echo.echo.set()


@dp.message_handler(text='⬅️ назад', state=Echo.echo)
async def channel(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы отменили ответ',
                           reply_markup=keyboard)

    await state.finish()


@dp.message_handler(state=Echo.echo)
async def answer_user(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    user_id = data.get("user_id")
    await bot.send_message(chat_id=user_id,
                           text=f'Вам написал администратор: {message.from_user.full_name}\n'
                                f'Ответ: {answer}')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')
    await message.answer(text=f'Сообщение пользователю отправлено умпешно\n',
                         reply_markup=keyboard)
    await state.finish()