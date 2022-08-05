from aiogram import types
from aiogram.dispatcher import FSMContext

from data.prolong_sub import prolong_sub
from filters import CheckUsers, CheckMaster, CheckClient
from loader import dp, bot
from states.state_users import Photo
from utils.db_api import postgres


@dp.message_handler(CheckUsers(), text='🖼 Фото профиля')
async def photo_of_works(message: types.Message):
    await prolong_sub(user_id=message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ назад')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Отправьте фото которое будет отображаться в вашем профиле',
                           reply_markup=keyboard)

    await Photo.photo_master.set()


@dp.message_handler(CheckMaster(), text='⬅️ назад', state=Photo.photo_master)
async def back(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💻 Социальные сети', '💅 Услуги')
    keyboard.row('🙋‍♀️О себе', '🖼 Фото профиля')
    keyboard.row('📂 Мой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы вернулись в меню редактирования профиля',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(CheckClient(), text='⬅️ назад', state=Photo.photo_master)
async def back(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💻 Социальные сети', '💅 Стать мастером')
    keyboard.row('🙋‍♀️О себе', '🖼 Фото профиля')
    keyboard.row('📂 Мой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы вернулись в меню редактирования профиля',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(CheckMaster(), content_types=types.ContentType.PHOTO, state=Photo.photo_master)
async def photo_master(message: types.Message, state: FSMContext):
    await message.photo[-1].download()
    photo_id = message.photo[-1].file_id
    user_id = message.from_user.id
    await postgres.update_photo(user_id=user_id, photo=photo_id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💻 Социальные сети', '💅 Услуги')
    keyboard.row('🙋‍♀️О себе', '🖼 Фото профиля')
    keyboard.row('📂 Мой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно обновили фото вашего профиля',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(CheckClient(), content_types=types.ContentType.PHOTO, state=Photo.photo_master)
async def photo_master(message: types.Message, state: FSMContext):
    await message.photo[-1].download()
    photo_id = message.photo[-1].file_id
    user_id = message.from_user.id
    await postgres.update_photo(user_id=user_id, photo=photo_id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💻 Социальные сети', '💅 Стать мастером')
    keyboard.row('🙋‍♀️О себе', '🖼 Фото профиля')
    keyboard.row('📂 Мой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы успешно обновили фото вашего профиля',
                           reply_markup=keyboard)
    await state.finish()
