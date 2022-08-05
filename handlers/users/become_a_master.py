from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton

from data.profile import profile_user, services_master
from filters import CheckClient
from loader import dp, bot
from states.state_users import Become_master, Reject
from utils.db_api import postgres


@dp.message_handler(CheckClient(), text='💅 Стать мастером')
async def become_a_master(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('👤 Отправить на проверку')
    keyboard.row('✍️Редактировать свой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Нажав на кнопку ниже Вы отправляете ваш профиль нам на проверку.\n'
                                'Обязательно зполните следующие поля:\n'
                                '❗️  🚇 Метро(Ближайшая станция до места вашей работы)\n'
                                '❗️  🏡 Адрес(Адрес вашей работы)\n'
                                '❗️  👤 ФИО\n'
                                '❗️  🖼 Фото профиля(На фотографии должны быть вы)\n'
                                '❗️  💻 Социальные сети(Какую-либо из социальных сетей)\n'
                                '\n'
                                'Без заполнения указанных полей профиль не будет подтвержден',
                           reply_markup=keyboard)
    await Become_master.profile.set()


@dp.message_handler(CheckClient(), text='✍️Редактировать свой профиль', state=Become_master.profile)
async def my_profile(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('💻 Социальные сети', '💅 Стать мастером')
    keyboard.row('🙋‍♀️О себе', '🖼 Фото профиля')
    keyboard.row('📂 Мой профиль')

    await bot.send_message(chat_id=message.from_user.id,
                           text='Чтобы повысить шанс выбора именно вас, заполните как можно больше информации',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(CheckClient(), text='👤 Отправить на проверку', state=Become_master.profile)
async def check_master(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user = await postgres.get_user(user_id=message.from_user.id)
    services = await services_master(user_id=message.from_user.id)
    if await postgres.check_rating_client(user_id=message.from_user.id):
        rating = await postgres.select_rating_client(user_id=message.from_user.id)
        keyboard = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Принять', callback_data=f"accept:{user_id}"),
                    InlineKeyboardButton(text='Отклонить', callback_data=f"reject:{user_id}")
                ]
            ]
        )
        await bot.send_photo(chat_id=1073644727,
                             photo=f"{user[0]['photo']}",
                             caption=profile_user(user=user, services=services, rating=rating),
                             reply_markup=keyboard)
        await bot.send_message(chat_id=message.from_user.id, text='Профиль успешно отправлен на проверку\n'
                                                                  'Вам придет оповещение о результате проверки')
        await state.finish()

    else:
        rating = 0
        keyboard = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Принять', callback_data=f"accept:{user_id}"),
                    InlineKeyboardButton(text='Отклонить', callback_data=f"reject:{user_id}")
                ]
            ]
        )
        await bot.send_photo(chat_id=-1001348703754,
                             photo=f"{user[0]['photo']}",
                             caption=profile_user(user=user, services=services, rating=rating),
                             reply_markup=keyboard)
        await bot.send_message(chat_id=message.from_user.id, text='Профиль успешно отправлен на проверку\n'
                                                                  'Вам придет оповещение о результате проверки')
        await state.finish()


@dp.callback_query_handler(text_contains='accept')
async def accept_master(call: types.CallbackQuery):
    user_id = call.data.split(":")[-1]
    user_id = int(user_id)
    await postgres.update_master(user_id=user_id, purse=0, manicure_pedicure='Нет', visage='Нет', hairdresser='Нет',
                                 other_services='Нет', favorites=0)
    await bot.send_message(chat_id=call.from_user.id, text='Профиль успешно подтвержден.\n')
    await bot.send_message(chat_id=user_id, text='Ваш профиль успешно подтвержден.\n'
                                                 'Поздравляем теперь вы мастер')


@dp.callback_query_handler(text_contains='reject')
async def accept_master(call: types.CallbackQuery, state: FSMContext):
    user_id = call.data.split(":")[-1]
    user_id = int(user_id)
    await state.update_data(user_id=user_id)
    await bot.send_message(chat_id=call.from_user.id, text='Напишите причину отказа в подтверждении.\n')
    await Reject.profile.set()


@dp.message_handler(state=Reject.profile)
async def check_master(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user_id = data.get("user_id")
    text = message.text
    await bot.send_message(chat_id=user_id, text=f'Вам отказали в подтверждении профиля на мастера\n'
                                                 f'Причина: {text}')
    await bot.send_message(chat_id=message.from_user.id, text='Сообщение успешно отправлено')
    await state.finish()
