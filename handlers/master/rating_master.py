from aiogram import types
from aiogram.types import InputFile

from loader import dp, bot
from utils.db_api import postgres


@dp.callback_query_handler(text='rating_master')
async def rating(call: types.CallbackQuery):
    if await postgres.check_master_in_recall(user_id=call.from_user.id):
        if await postgres.check_rating_master(user_id=call.from_user.id):
            recall = await postgres.get_last_recall_master(user_id=call.from_user.id)
            rating = await postgres.select_rating_master(user_id=call.from_user.id)
            text = ''
            if 1 <= rating[0]['avg'] < 2:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️({round(float(rating[0]['avg']), 1)})"

            elif 2 <= rating[0]['avg'] < 3:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️⭐️ ({round(float(rating[0]['avg']), 1)})"

            elif 3 <= rating[0]['avg'] < 4:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️⭐️⭐️ ({round(float(rating[0]['avg']), 1)})"

            elif 4 <= rating[0]['avg'] < 5:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️⭐️⭐️⭐️ ({round(float(rating[0]['avg']), 1)})"

            elif 5 <= rating[0]['avg']:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️⭐️⭐️⭐️⭐️ ({round(float(rating[0]['avg']), 1)})"
            text_recall = ''
            for re in recall:
                text_recall += f"🗣 {re['name_recall']}: {re['recall']}\n"
            await bot.send_message(chat_id=call.from_user.id,
                                   text=f"{text}\n\n"
                                        f"Последнии отзывы о вас:\n"
                                        f"{text_recall}")
            await bot.send_document(chat_id=call.from_user.id,
                                    document=InputFile(f"feedback_master/{call.from_user.id}.txt"),
                                    caption='Все отзывы о вас')
        else:
            recall = await postgres.get_last_recall_master(user_id=call.from_user.id)
            text = ''
            text_recall = ''
            for re in recall:
                text += f"🗣 {re['name_recall']}: {re['recall']}\n"
            await bot.send_message(chat_id=call.from_user.id,
                                   text=f"🏅 Ваш рейтинг: Оценка отсутствует\n\n"
                                        f"Последнии отзывы о вас:\n"
                                        f"{text_recall}")
            await bot.send_document(chat_id=call.from_user.id,
                                    document=InputFile(f"feedback_master/{call.from_user.id}.txt"),
                                    caption='Все отзывы о вас')

    else:
        if await postgres.check_rating_master(user_id=call.from_user.id):
            rating = await postgres.select_rating_master(user_id=call.from_user.id)
            text = ''
            if 1 <= rating[0]['avg'] < 2:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️({round(float(rating[0]['avg']), 1)})"

            elif 2 <= rating[0]['avg'] < 3:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️⭐️ ({round(float(rating[0]['avg']), 1)})"

            elif 3 <= rating[0]['avg'] < 4:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️⭐️⭐️ ({round(float(rating[0]['avg']), 1)})"

            elif 4 <= rating[0]['avg'] < 5:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️⭐️⭐️⭐️ ({round(float(rating[0]['avg']), 1)})"

            elif 5 <= rating[0]['avg']:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️⭐️⭐️⭐️⭐️ ({round(float(rating[0]['avg']), 1)})"
            await bot.send_message(chat_id=call.from_user.id,
                                   text=f"{text}\n"
                                        f"Отзывы о вас отсутствуют")

        else:
            await bot.send_message(chat_id=call.from_user.id,
                                   text=f"🏅 Ваш рейтинг: Оценка отсутствует\n\n"
                                        f"Последнии отзывы о вас: Отзывы отсутствуют")

@dp.callback_query_handler(text='rating_client')
async def rating(call: types.CallbackQuery):
    if await postgres.check_recall_client(user_id=call.from_user.id):
        if await postgres.check_rating_client(user_id=call.from_user.id):
            recall = await postgres.get_last_recall_client(user_id=call.from_user.id)
            rating = await postgres.select_rating_client(user_id=call.from_user.id)
            text = ''
            if 1 <= rating[0]['avg'] < 2:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️({round(float(rating[0]['avg']), 1)})"

            elif 2 <= rating[0]['avg'] < 3:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️⭐️ ({round(float(rating[0]['avg']), 1)})"

            elif 3 <= rating[0]['avg'] < 4:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️⭐️⭐️ ({round(float(rating[0]['avg']), 1)})"

            elif 4 <= rating[0]['avg'] < 5:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️⭐️⭐️⭐️ ({round(float(rating[0]['avg']), 1)})"

            elif 5 <= rating[0]['avg']:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️⭐️⭐️⭐️⭐️ ({round(float(rating[0]['avg']), 1)})"
            text_recall = ''
            for re in recall:
                text_recall += f"🗣 {re['name_recall']}: {re['recall']}\n"
            await bot.send_message(chat_id=call.from_user.id,
                                   text=f"{text}\n\n"
                                        f"Последнии отзывы о вас:\n"
                                        f"{text}")
            await bot.send_document(chat_id=call.from_user.id,
                                    document=InputFile(f"feedback_client/{call.from_user.id}.txt"),
                                    caption='Все отзывы о вас')
        else:
            recall = await postgres.get_last_recall_client(user_id=call.from_user.id)
            text = ''
            for re in recall:
                text += f"🗣 {re['name_recall']}: {re['recall']}\n"
            await bot.send_message(chat_id=call.from_user.id,
                                   text=f"🏅 Ваш рейтинг: Оценка отсутствует\n\n"
                                        f"Последнии отзывы о вас:\n"
                                        f"{text}")
            await bot.send_document(chat_id=call.from_user.id,
                                    document=InputFile(f"feedback_client/{call.from_user.id}.txt"),
                                    caption='Все отзывы о вас')

    else:
        if await postgres.check_rating_client(user_id=call.from_user.id):
            rating = await postgres.select_rating_client(user_id=call.from_user.id)
            text = ''
            if 1 <= rating[0]['avg'] < 2:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️({round(float(rating[0]['avg']), 1)})"

            elif 2 <= rating[0]['avg'] < 3:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️⭐️ ({round(float(rating[0]['avg']), 1)})"

            elif 3 <= rating[0]['avg'] < 4:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️⭐️⭐️ ({round(float(rating[0]['avg']), 1)})"

            elif 4 <= rating[0]['avg'] < 5:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️⭐️⭐️⭐️ ({round(float(rating[0]['avg']), 1)})"

            elif 5 <= rating[0]['avg']:
                text += f"🏅 <b>Ваш рейтинг</b>: ⭐️⭐️⭐️⭐️⭐️ ({round(float(rating[0]['avg']), 1)})"
            await bot.send_message(chat_id=call.from_user.id,
                                   text=f"{text}\n"
                                        f"Отзывы о вас отсутствуют")

        else:
            await bot.send_message(chat_id=call.from_user.id,
                                   text=f"🏅 Ваш рейтинг: Оценка отсутствует\n\n"
                                        f"Последнии отзывы о вас: Отзывы отсутствуют")