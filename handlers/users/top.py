from aiogram import types
from aiogram.types import InlineKeyboardButton

from loader import dp, bot
from utils.db_api import postgres


@dp.callback_query_handler(text='top')
async def top(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='💅 Маникюр/Педикюр', callback_data='top_manicure')
            ],
            [
                InlineKeyboardButton(text='💇‍♀️Парикмахер', callback_data='top_hairdresser')
            ],
            [
                InlineKeyboardButton(text='💋 Визаж', callback_data='top_visage')
            ],
            [
                InlineKeyboardButton(text='🧖‍♀️Другие услуги', callback_data='top_other_services')
            ],
            [
                InlineKeyboardButton(text='⬅️ Назад', callback_data='back_find')
            ]

        ]
    )
    await call.message.edit_text(text='Выберите услугу в которой хотите увидеть топ 25 мастеров')
    await call.message.edit_reply_markup(reply_markup=keyboard)


@dp.callback_query_handler(text='top_manicure')
async def top(call: types.CallbackQuery):
    city = await postgres.select_city(user_id=call.from_user.id)
    master = await postgres.select_top_master_manicure(city=city[0]['city'])
    if master != []:
        c = 0
        top_text = ''
        for user in master:
            if user['best'] == True:
                text = ''
                if 1 <= user['avg'] < 2:
                    text += f"⭐️({round(float(user['avg']), 1)})"

                elif 2 <= user['avg'] < 3:
                    text += f"⭐️⭐️ ({round(float(user['avg']), 1)})"

                elif 3 <= user['avg'] < 4:
                    text += f"⭐️⭐️⭐️ ({round(float(user['avg']), 1)})"

                elif 4 <= user['avg'] < 5:
                    text += f"⭐️⭐️⭐️⭐️ ({round(float(user['avg']), 1)})"

                elif 5 <= user['avg']:
                    text += f"⭐️⭐️⭐️⭐️⭐️ ({round(float(user['avg']), 1)})"
                c += 1
                top_text += f"{c}. {user['name_user']}(ID:{user['user_number']}): {text}\n\n"

        await bot.send_message(chat_id=call.from_user.id, text=f"Топ лучших мастеров в услуге маникюр/педикюр:\n\n"
                                                               f"{top_text}")
    else:
        await bot.send_message(chat_id=call.from_user.id, text=f"В вашем городе еще не сформировался топ мастеров в услуге парикмахер")


@dp.callback_query_handler(text='top_hairdresser')
async def top(call: types.CallbackQuery):
    city = await postgres.select_city(user_id=call.from_user.id)
    master = await postgres.select_top_master_hairdresser(city=city[0]['city'])
    if master != []:
        c = 0
        top_text = ''
        for user in master:
            if user['best'] == True:
                text = ''
                if 1 <= user['avg'] < 2:
                    text += f"⭐️({round(float(user['avg']), 1)})"

                elif 2 <= user['avg'] < 3:
                    text += f"⭐️⭐️ ({round(float(user['avg']), 1)})"

                elif 3 <= user['avg'] < 4:
                    text += f"⭐️⭐️⭐️ ({round(float(user['avg']), 1)})"

                elif 4 <= user['avg'] < 5:
                    text += f"⭐️⭐️⭐️⭐️ ({round(float(user['avg']), 1)})"

                elif 5 <= user['avg']:
                    text += f"⭐️⭐️⭐️⭐️⭐️ ({round(float(user['avg']), 1)})"
                c += 1
                top_text += f"{c}. {user['name_user']}(ID:{user['user_number']}): {text}\n\n"

        await bot.send_message(chat_id=call.from_user.id, text=f"Топ лучших мастеров в услуге парикмахер:\n\n"
                                                               f"{top_text}")
    else:
        await bot.send_message(chat_id=call.from_user.id, text=f"В вашем городе еще не сформировался топ мастеров в услуге парикмахер")


@dp.callback_query_handler(text='top_visage')
async def top(call: types.CallbackQuery):
    city = await postgres.select_city(user_id=call.from_user.id)
    master = await postgres.select_top_master_visage(city=city[0]['city'])
    if master != []:
        c = 0
        top_text = ''
        for user in master:
            if user['best'] == True:
                text = ''
                if 1 <= user['avg'] < 2:
                    text += f"⭐️({round(float(user['avg']), 1)})"

                elif 2 <= user['avg'] < 3:
                    text += f"⭐️⭐️ ({round(float(user['avg']), 1)})"

                elif 3 <= user['avg'] < 4:
                    text += f"⭐️⭐️⭐️ ({round(float(user['avg']), 1)})"

                elif 4 <= user['avg'] < 5:
                    text += f"⭐️⭐️⭐️⭐️ ({round(float(user['avg']), 1)})"

                elif 5 <= user['avg']:
                    text += f"⭐️⭐️⭐️⭐️⭐️ ({round(float(user['avg']), 1)})"
                c += 1
                top_text += f"{c}. {user['name_user']}(ID:{user['user_number']}): {text}\n\n"

        await bot.send_message(chat_id=call.from_user.id, text=f"Топ лучших мастеров в услуге визаж:\n\n"
                                                               f"{top_text}")
    else:
        await bot.send_message(chat_id=call.from_user.id, text=f"В вашем городе еще не сформировался топ мастеров в услуге визаж")

@dp.callback_query_handler(text='top_other_services')
async def top(call: types.CallbackQuery):
    city = await postgres.select_city(user_id=call.from_user.id)
    master = await postgres.select_top_master_other_services(city=city[0]['city'])
    if master != []:
        c = 0
        top_text = ''
        for user in master:
            if user['best'] == True:
                text = ''
                if 1 <= user['avg'] < 2:
                    text += f"⭐️({round(float(user['avg']), 1)})"

                elif 2 <= user['avg'] < 3:
                    text += f"⭐️⭐️ ({round(float(user['avg']), 1)})"

                elif 3 <= user['avg'] < 4:
                    text += f"⭐️⭐️⭐️ ({round(float(user['avg']), 1)})"

                elif 4 <= user['avg'] < 5:
                    text += f"⭐️⭐️⭐️⭐️ ({round(float(user['avg']), 1)})"

                elif 5 <= user['avg']:
                    text += f"⭐️⭐️⭐️⭐️⭐️ ({round(float(user['avg']), 1)})"
                c += 1
                top_text += f"{c}. {user['name_user']}(ID:{user['user_number']}): {text}\n\n"

        await bot.send_message(chat_id=call.from_user.id, text=f"Топ лучших мастеров в других услугах:\n\n"
                                                               f"{top_text}")
    else:
        await bot.send_message(chat_id=call.from_user.id, text=f"В вашем городе еще не сформировался топ мастеров других услуг")