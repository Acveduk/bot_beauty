from aiogram import types
from aiogram.types import KeyboardButton

from utils.db_api import postgres


def manicure_keyboard(services_manicure):
    manicure = ''
    pedicure = ''
    if services_manicure[0]['manicure'] == 'Да':
        manicure += '🖐 Маникюр ✅'
    else:
        manicure += '🖐 Маникюр ❌'

    if services_manicure[0]['pedicure'] == 'Да':
        pedicure += '🦶 Педикюр ✅'
    else:
        pedicure += '🦶 Педикюр ❌'

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(f'{manicure}', f'{pedicure}')
    keyboard.row(f'💅 Услуги')

    return keyboard


def visage_keyboard(services_visage):
    makeup = ''
    eyebrows = ''
    eyelashes = ''
    wedding_image = ''
    if services_visage[0]['makeup'] == 'Да':
        makeup += '💋 Макияж ✅'
    else:
        makeup += '💋 Макияж ❌'

    if services_visage[0]['eyebrows'] == 'Да':
        eyebrows += '👁 Брови ✅'
    else:
        eyebrows += '👁 Брови ❌'

    if services_visage[0]['eyelashes'] == 'Да':
        eyelashes += '👀 Ресницы ✅'
    else:
        eyelashes += '👀 Ресницы ❌'

    if services_visage[0]['wedding_image'] == 'Да':
        wedding_image += '👰‍ Свадебный образ ✅'
    else:
        wedding_image += '👰‍ Свадебный образ ❌'

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(f'{makeup}', f'{eyebrows}')
    keyboard.row(f'{eyelashes}', f'{wedding_image}')
    keyboard.row(f'💅 Услуги')

    return keyboard


def hairdresser_keyboard(services_hairdresser):
    haircut = ''
    man_haircut = ''
    hair_styling = ''
    hair_coloring = ''
    hair_care = ''
    if services_hairdresser[0]['haircut'] == 'Да':
        haircut += '💇‍♀️Стрижка ✅'
    else:
        haircut += '💇‍♀️Стрижка ❌'

    if services_hairdresser[0]['man_haircut'] == 'Да':
        man_haircut += '💇‍♂️Мужская стрижка ✅'
    else:
        man_haircut += '💇‍♂️Мужская стрижка ❌'

    if services_hairdresser[0]['hair_styling'] == 'Да':
        hair_styling += '💆‍♀️Укладка и прически ✅'
    else:
        hair_styling += '💆‍♀️Укладка и прически ❌'

    if services_hairdresser[0]['hair_coloring'] == 'Да':
        hair_coloring += '👩‍🦰 Окрашивание ✅'
    else:
        hair_coloring += '👩‍🦰 Окрашивание ❌'

    if services_hairdresser[0]['hair_care'] == 'Да':
        hair_care += '👩‍⚕️Уход и лечение ✅'
    else:
        hair_care += '👩‍⚕️Уход и лечение ❌'

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(f'{haircut}', f'{man_haircut}')
    keyboard.row(f'{hair_styling}', f'{hair_coloring}')
    keyboard.row(f'{hair_care}')
    keyboard.row(f'💅 Услуги')

    return keyboard


def other_services_keyboard(services_other_services):
    massage = ''
    depilation_with_wax = ''
    shugaring = ''
    tan_at_home = ''
    if services_other_services[0]['massage'] == 'Да':
        massage += '💆‍♀️Массаж ✅'
    else:
        massage += '💆‍♀️Массаж ❌'

    if services_other_services[0]['depilation_with_wax'] == 'Да':
        depilation_with_wax += '👩‍⚕️Депиляция воском ✅'
    else:
        depilation_with_wax += '👩‍⚕️Депиляция воском ❌'

    if services_other_services[0]['shugaring'] == 'Да':
        shugaring += '🧖‍♀️Шугаринг ✅'
    else:
        shugaring += '🧖‍♀️Шугаринг ❌'

    if services_other_services[0]['tan_at_home'] == 'Да':
        tan_at_home += '🧴 Загар дома ✅'
    else:
        tan_at_home += '🧴 Загар дома ❌'

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(f'{massage}', f'{tan_at_home}')
    keyboard.row(f'{depilation_with_wax}', f'{shugaring}')
    keyboard.row(f'💅 Услуги')

    return keyboard
