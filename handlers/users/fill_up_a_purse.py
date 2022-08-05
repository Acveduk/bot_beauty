from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hlink, hcode

from loader import dp, bot
from states.state_users import Purse
from utils.db_api import postgres
from utils.misc.qiwi import Payment, NoPaymentFound, NotEnoughMoney


@dp.callback_query_handler(text='replenish')
async def sub(call: types.CallbackQuery):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('⬅️ назад')
    await bot.send_message(chat_id=call.from_user.id,
                           text='Введите сумму на которую хотите пожертвовать',
                           reply_markup=keyboard)
    await Purse.sum.set()


@dp.message_handler(text='⬅️ назад', state=Purse.sum)
async def channel(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы отменили пополнения кошелька',
                           reply_markup=keyboard)
    await state.finish()


@dp.message_handler(state=Purse.sum)
async def sum(message: types.Message, state: FSMContext):
    try:
        amount = int(message.text)
        payment = Payment(amount=amount)
        payment.create()

        paid_keyboard = types.InlineKeyboardMarkup()
        paid_keyboard.add(types.KeyboardButton(text='Оплатить', url=payment.invoice))
        paid_keyboard.add(types.KeyboardButton(text='Подтвердить произведенную оплату', callback_data="paid"))
        paid_keyboard.add(types.KeyboardButton(text='Отмена', callback_data="cancel"))

        await message.answer(
            "\n".join([
                f"Оплатите не меньше {amount:.2f} по номеру телефона или по адресу",
                "",
                hlink(title='Нажми на меня чтобы оплатить\n', url=payment.invoice),
                "И обязательно укажите ID платежа",
                hcode(payment.id)
            ]),
            reply_markup=paid_keyboard
        )
        await Purse.qiwi.set()
        await state.update_data(amount=payment.amount)
        await state.update_data(id=payment.id)
    except ValueError:
        await bot.send_message(chat_id=message.from_user.id,
                               text='Введите число')
        await Purse.sum.set()


@dp.message_handler(text='⬅️ назад', state=Purse.qiwi)
async def channel(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Вы отменили пополнения кошелька',
                           reply_markup=keyboard)
    await state.finish()


@dp.callback_query_handler(text="cancel", state=Purse.qiwi)
async def cancel_payment(call: types.CallbackQuery, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')
    await call.message.edit_reply_markup()
    await bot.send_message(chat_id=call.from_user.id,
                           text='Вы отменили пополнения кошелька',
                           reply_markup=keyboard)
    await state.finish()


@dp.callback_query_handler(text="paid", state=Purse.qiwi)
async def approve_payment(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    amount = data.get("amount")
    id = data.get("id")
    payment = Payment(amount=amount, id=id)
    try:
        payment.check_payment()
    except NoPaymentFound:
        await call.message.answer("Транзакция не найдена.")
        return
    except NotEnoughMoney:
        await call.message.answer("Оплаченная сума меньше необходимой.")
        return

    else:
        user_id = call.from_user.id
        price = data.get("amount")
        pay_id = data.get("id")
        purse_master = await postgres.purse(user_id=call.from_user.id)
        purse = int(purse_master[0]['purse']) + price
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('ОК')

        await postgres.update_purse_master(user_id=user_id, purse=purse, pay_id=pay_id)
        await call.message.answer("Успешно оплачено", reply_markup=keyboard)

    await Purse.ok.set()


@dp.message_handler(text='ОК', state=Purse.ok)
async def channel(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('❤️Избранное', '📝 Создать заявку на услугу')
    keyboard.row('🏅 Найти мастера по рейтингу', '💬 Канал/Чат')
    keyboard.row('💰 Кошелек', '📂 Мой профиль')
    keyboard.row('ℹ️Как работать с ботом')
    await bot.send_message(chat_id=message.from_user.id,
                           text='Кошелек успешно пополнен',
                           reply_markup=keyboard)
    await state.finish()
