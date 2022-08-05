from aiogram import types
from aiogram.types import InlineKeyboardButton


def sub_keyboard(services):
    manicure_pedicure = ''
    hairdresser = ''
    visage = ''
    other_services = ''
    call_manicure = ''
    call_hairdresser = ''
    call_visage = ''
    call_other_services = ''
    if services[0]['manicure_pedicure'] == 'Да':
        manicure_pedicure += '💅 Маникюр/Педикюр ✅'
        call_manicure += 'manicure+'
    else:
        manicure_pedicure += '💅 Маникюр/Педикюр ❌'
        call_manicure += 'manicure-'

    if services[0]['hairdresser'] == 'Да':
        hairdresser += '💇‍♀️Парикмахер ✅'
        call_hairdresser += 'hairdresser+'
    else:
        hairdresser += '💇‍♀️Парикмахер ❌'
        call_hairdresser += 'hairdresser-'

    if services[0]['visage'] == 'Да':
        visage += '💋 Визаж ✅'
        call_visage += 'visage+'
    else:
        visage += '💋 Визаж ❌'
        call_visage += 'visage-'

    if services[0]['other_services'] == 'Да':
        other_services += '🧖‍♀️Другие услуги ✅'
        call_other_services += 'other_services+'
    else:
        other_services += '🧖‍♀️Другие услуги ❌'
        call_other_services += 'other_services-'

    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f'{manicure_pedicure}', callback_data=f'{call_manicure}')
            ],
            [
                InlineKeyboardButton(text=f'{hairdresser}', callback_data=f'{call_hairdresser}')
            ],
            [
                InlineKeyboardButton(text=f'{visage}', callback_data=f'{call_visage}')
            ],
            [
                InlineKeyboardButton(text=f'{other_services}', callback_data=f'{call_other_services}')
            ],
            [
                InlineKeyboardButton(text='⬅️ назад', callback_data='back')
            ]
        ]
    )

    return keyboard



