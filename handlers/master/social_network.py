from aiogram import types
from aiogram.dispatcher import FSMContext

from data.prolong_sub import prolong_sub
from filters import CheckUsers
from loader import dp, bot
from states.state_users import Vk, Insta, Telegram
from utils.db_api import postgres


@dp.message_handler(CheckUsers(), text='💻 Социальные сети')
async def edit_profile(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💻 Вконтакте')
    keyboard.row('💻 Instagram')
    keyboard.row('💻 Телеграм')
    keyboard.row('✍️Редактировать свой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Чтобы повысить шанс выбора именно вас, заполните как можно больше информации',
                           reply_markup=keyboard)


@dp.message_handler(CheckUsers(), text='💻 Вконтакте')
async def vk(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ назад')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Пришлите ссылку на вашу страницу Вконтакте',
                           reply_markup=keyboard)

    await Vk.vk_link.set()


@dp.message_handler(CheckUsers(), text='⬅️ назад', state=Vk.vk_link)
async def back(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💻 Вконтакте')
    keyboard.row('💻 Instagram')
    keyboard.row('💻 Телеграм')
    keyboard.row('✍️Редактировать свой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы вернулись в меню редактирования профиля',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(CheckUsers(), state=Vk.vk_link)
async def back(message: types.Message, state: FSMContext):
    vk_link = message.text
    user_id = message.from_user.id
    await postgres.update_vk(user_id=user_id, vk=vk_link)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💻 Вконтакте')
    keyboard.row('💻 Instagram')
    keyboard.row('💻 Телеграм')
    keyboard.row('✍️Редактировать свой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно обновили ссылку на страницу Вконтакте',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(CheckUsers(), text='💻 Instagram')
async def insta(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ назад')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Пришлите ссылку на вашу страницу в Instagram',
                           reply_markup=keyboard)

    await Insta.insta_link.set()


@dp.message_handler(CheckUsers(), text='⬅️ назад', state=Insta.insta_link)
async def back(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💻 Вконтакте')
    keyboard.row('💻 Instagram')
    keyboard.row('💻 Телеграм')
    keyboard.row('✍️Редактировать свой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы вернулись в меню редактирования профиля',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(CheckUsers(), state=Insta.insta_link)
async def back(message: types.Message, state: FSMContext):
    insta_link = message.text
    user_id = message.from_user.id
    await postgres.update_insta(user_id=user_id, insta=insta_link)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💻 Вконтакте')
    keyboard.row('💻 Instagram')
    keyboard.row('💻 Телеграм')
    keyboard.row('✍️Редактировать свой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно обновили ссылку на страницу в Instagram',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(CheckUsers(), text='💻 Телеграм')
async def insta(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ назад')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Пришлите ссылку на ваш канал в Telegram',
                           reply_markup=keyboard)

    await Telegram.tg_link.set()


@dp.message_handler(CheckUsers(), text='⬅️ назад', state=Telegram.tg_link)
async def back(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💻 Вконтакте')
    keyboard.row('💻 Instagram')
    keyboard.row('💻 Телеграм')
    keyboard.row('✍️Редактировать свой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы вернулись в меню редактирования профиля',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(CheckUsers(), state=Telegram.tg_link)
async def back(message: types.Message, state: FSMContext):
    tg_link = message.text
    user_id = message.from_user.id
    await postgres.update_tg(user_id=user_id, telegram=tg_link)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💻 Вконтакте')
    keyboard.row('💻 Instagram')
    keyboard.row('💻 Телеграм')
    keyboard.row('✍️Редактировать свой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно обновили ссылку на канал в Telegram',
                           reply_markup=keyboard)
    await state.finish()
