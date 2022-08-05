from aiogram import types
from aiogram.dispatcher import FSMContext

from data.prolong_sub import prolong_sub
from filters import CheckUsers
from loader import dp, bot
from states.state_users import Question, Answer


@dp.message_handler(CheckUsers(), text='ℹ️Как работать с ботом')
async def bot_start(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('📜 Инструкция', '❓ Вопрос/Ответ')
    keyboard.row('⬅️ назад')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Добро пожаловать. Бот создан для того, чтобы сводить мастеров и клиентов',
                           reply_markup=keyboard)


@dp.message_handler(CheckUsers(), text='📜 Инструкция')
async def bot_start(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Посмотреть', url="https://t.me/testchannalmy"),
                 types.InlineKeyboardButton(text='Прочитать', url="https://t.me/testchannalmy"))
    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите как вам удобнее изучить инструкцию по работе с ботом',
                           reply_markup=keyboard)


@dp.message_handler(CheckUsers(), text='❓ Вопрос/Ответ', state=None)
async def feedback_user(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ назад')
    await message.answer(text=f'Введите ваш вопрос', reply_markup=keyboard)

    await Question.question.set()


@dp.message_handler(text='⬅️ назад', state=Question.question)
async def channel(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы отменили вопрос',
                           reply_markup=keyboard)

    await state.finish()


@dp.message_handler(state=Question.question)
async def answer_user(message: types.Message, state: FSMContext):
    user_message = message.text
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Перенаправить в бота', callback_data=f"answer:{message.from_user.id}"))

    await bot.send_message(chat_id=-1001348703754,
                           text=f'У вас новый вопрос от пользователя: {message.from_user.full_name}\n'
                                f'id пользователя: {message.from_user.id}\n'
                                f'Вопрос: {user_message}',
                           reply_markup=keyboard)

    keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard2.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard2.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard2.row('💰 Кошелек', '📂 Мой профиль')
    keyboard2.row('ℹ️Как работать с ботом')

    await message.answer(text=f'Администратору бота отправлен ваш вопрос\n'
                              f'Он постарается ответить как можно быстрее',
                         reply_markup=keyboard2)
    await state.finish()


@dp.callback_query_handler(text_contains="answer")
async def cancel_payment(call: types.CallbackQuery, state: FSMContext):
    user_id = call.data.split(":")[-1]
    user_id = int(user_id)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Ответить', callback_data=f"user:{user_id}"))

    keyboard2 = types.InlineKeyboardMarkup()
    keyboard2.add(types.InlineKeyboardButton(text='Перейти в бота', url=f"https://t.me/PoiskMasteraBot"))
    await call.message.edit_reply_markup(reply_markup=keyboard2)
    await bot.send_message(chat_id=call.from_user.id,
                           text='Нажмите на кнопку, чтобы ответить пользователю',
                           reply_markup=keyboard)


@dp.callback_query_handler(text_contains="user")
async def cancel_payment(call: types.CallbackQuery, state: FSMContext):
    user_id = call.data.split(":")[-1]
    user_id = int(user_id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ назад')
    await state.update_data(user_id=user_id)
    await bot.send_message(chat_id=call.from_user.id,
                           text='Введите ответ пользователю',
                           reply_markup=keyboard)
    await Answer.answer2.set()


@dp.message_handler(text='⬅️ назад', state=Answer.answer2)
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


@dp.message_handler(state=Answer.answer2)
async def answer_user(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    user_id = data.get("user_id")
    await bot.send_message(chat_id=user_id,
                           text=f'Вам ответил администратор: {message.from_user.full_name}\n'
                                f'Ответ: {answer}')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')
    await message.answer(text=f'Сообщение пользователю отправлено умпешно\n',
                         reply_markup=keyboard)
    await state.finish()
