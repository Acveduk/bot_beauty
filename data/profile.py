from utils.db_api import postgres


def profile_user(user, services, rating):
    text = f"Ваш профиль:\n" \
           f"👤 <b>ID пользователя</b>: {user[0]['user_number']}\n" \
           f"📱 <b>Номер телефона</b>: {user[0]['phone_number']}\n"
    ser = ', '.join(services)
    if user[0]['city'] != 'Пусто':
        text += f"🏙 <b>Город</b>: {user[0]['city']}\n\n"

    if user[0]['manicure_pedicure'] == 'Да' or user[0]['hairdresser'] == 'Да' or user[0]['visage'] == 'Да' or \
            user[0]['other_services'] == 'Да':
        text += f"💅 <b>Услуги</b>: {ser}\n\n"

    if user[0]['fio'] != 'Пусто':
        text += f"👤 <b>ФИО</b>: {user[0]['fio']}\n\n"

    if user[0]['metro'] != 'Пусто':
        text += f"🚇 <b>Метро</b>:{user[0]['metro']}\n"

    if user[0]['address'] != 'Пусто':
        text += f"🏡 <b>Адрес</b>:{user[0]['address']}\n\n"

    if user[0]['vk'] != 'Пусто':
        text += f"💻 <a href='{user[0]['vk']}'><b>Вконтакте</b></a>\n"

    if user[0]['insta'] != 'Пусто':
        text += f"💻 <a href='{user[0]['insta']}'><b>Instagram</b></a>\n"

    if user[0]['telegram'] != 'Пусто':
        text += f"💻 <a href='{user[0]['telegram']}'><b>Телеграм</b></a>\n"

    if user[0]['about_me'] != 'Пусто':
        text += f"\n🙋‍♀️<b>О себе</b>: {user[0]['about_me']}\n"

    if user[0]['favorites'] >= 0:
        text += f"\n☑️<b>Добавили в избранное</b>: {user[0]['favorites']}\n"

    if rating == 0:
        text += f"\n🏅 <b>Рейтинг</b>: Оценка отсутствует\n\n"

    elif 1 <= rating[0]['avg'] < 2:
        text += f"🏅 <b>Рейтинг</b>: ⭐️({round(float(rating[0]['avg']), 1)})\n\n"

    elif 2 <= rating[0]['avg'] < 3:
        text += f"🏅 <b>Рейтинг</b>: ⭐️⭐️ ({round(float(rating[0]['avg']), 1)})\n\n"

    elif 3 <= rating[0]['avg'] < 4:
        text += f"🏅 <b>Рейтинг</b>: ⭐️⭐️⭐️ ({round(float(rating[0]['avg']), 1)})\n\n"

    elif 4 <= rating[0]['avg'] < 5:
        text += f"🏅 <b>Рейтинг</b>: ⭐️⭐️⭐️⭐️ ({round(float(rating[0]['avg']), 1)})\n\n"

    elif 5 <= rating[0]['avg']:
        text += f"🏅 <b>Рейтинг</b>: ⭐️⭐️⭐️⭐️⭐️ ({round(float(rating[0]['avg']), 1)})\n\n"

    text += f"Чтобы редактировать профиль нажмите ниже ⬇️"
    return text


def find_master(master, rating, services):
    text = f"👤 <b>ID пользователя</b>: {master[0]['user_number']}\n"
    ser = ', '.join(services)
    if master[0]['city'] != 'Пусто':
        text += f"🏙 <b>Город</b>: {master[0]['city']}\n\n"

    if master[0]['manicure_pedicure'] == 'Да' or master[0]['hairdresser'] == 'Да' or master[0]['visage'] == 'Да' or \
            master[0]['other_services'] == 'Да':
        text += f"💅 <b>Услуги</b>: {ser}\n\n"

    if master[0]['fio'] != 'Пусто':
        text += f"👤 <b>ФИО</b>: {master[0]['fio']}\n\n"

    if master[0]['metro'] != 'Пусто':
        text += f"🚇 <b>Метро</b>:{master[0]['metro']}\n"

    if master[0]['address'] != 'Пусто':
        text += f"🏡 <b>Адрес</b>:{master[0]['address']}\n\n"

    if master[0]['vk'] != 'Пусто':
        text += f"💻 <a href='{master[0]['vk']}'><b>Вконтакте</b></a>\n"

    if master[0]['insta'] != 'Пусто':
        text += f"💻 <a href='{master[0]['insta']}'><b>Instagram</b></a>\n"

    if master[0]['telegram'] != 'Пусто':
        text += f"💻 <a href='{master[0]['telegram']}'><b>Телеграм</b></a>\n"

    if master[0]['about_me'] != 'Пусто':
        text += f"\n🙋‍♀️<b>О себе</b>: {master[0]['about_me']}\n"

    if master[0]['favorites'] >= 0:
        text += f"\n☑️<b>Добавили в избранное</b>: {master[0]['favorites']}\n"

    if rating == 0:
        text += f"\n🏅 <b>Рейтинг</b>: Оценка отсутствует\n\n"

    elif 1 <= rating[0]['avg'] < 2:
        text += f"🏅 <b>Рейтинг</b>: ⭐️({round(float(rating[0]['avg']), 1)})\n\n"

    elif 2 <= rating[0]['avg'] < 3:
        text += f"🏅 <b>Рейтинг</b>: ⭐️⭐️ ({round(float(rating[0]['avg']), 1)})\n\n"

    elif 3 <= rating[0]['avg'] < 4:
        text += f"🏅 <b>Рейтинг</b>: ⭐️⭐️⭐️ ({round(float(rating[0]['avg']), 1)})\n\n"

    elif 4 <= rating[0]['avg'] < 5:
        text += f"🏅 <b>Рейтинг</b>: ⭐️⭐️⭐️⭐️ ({round(float(rating[0]['avg']), 1)})\n\n"

    elif 5 <= rating[0]['avg']:
        text += f"🏅 <b>Рейтинг</b>: ⭐️⭐️⭐️⭐️⭐️ ({round(float(rating[0]['avg']), 1)})\n\n"

    return text


async def services_master(user_id: int):
    services = []
    sub = await postgres.get_sub_master(user_id=user_id)
    if sub[0]['manicure_pedicure'] == 'Да':
        if await postgres.check_master_in_manicure(user_id=user_id):
            manicure_pedicure = await postgres.get_manicure(user_id=user_id)
            if manicure_pedicure[0]['manicure'] == 'Да':
                services.append('маникюр')
            if manicure_pedicure[0]['pedicure'] == 'Да':
                services.append('педикюр')

    if sub[0]['visage'] == 'Да':
        if await postgres.check_master_in_visage(user_id=user_id):
            visage = await postgres.check_visage(user_id=user_id)
            if visage[0]['makeup'] == 'Да':
                services.append('макияж')
            if visage[0]['eyebrows'] == 'Да':
                services.append('брови')
            if visage[0]['eyelashes'] == 'Да':
                services.append('ресницы')
            if visage[0]['wedding_image'] == 'Да':
                services.append('свадебный образ')

    if sub[0]['other_services'] == 'Да':
        if await postgres.check_master_in_other_services(user_id=user_id):
            other_services = await postgres.check_other_services(user_id=user_id)
            if other_services[0]['massage'] == 'Да':
                services.append('массаж')
            if other_services[0]['depilation_with_wax'] == 'Да':
                services.append('депиляция воском')
            if other_services[0]['shugaring'] == 'Да':
                services.append('шугаринг')
            if other_services[0]['tan_at_home'] == 'Да':
                services.append('загар дома')

    if sub[0]['hairdresser'] == 'Да':
        if await postgres.check_master_in_hairdresser(user_id=user_id):
            hairdresser = await postgres.check_hairdresser(user_id=user_id)
            if hairdresser[0]['haircut'] == 'Да':
                services.append('стрижка')
            if hairdresser[0]['man_haircut'] == 'Да':
                services.append('мужская стрижка')
            if hairdresser[0]['hair_styling'] == 'Да':
                services.append('укладка и прически')
            if hairdresser[0]['hair_coloring'] == 'Да':
                services.append('окрашивание')
            if hairdresser[0]['hair_care'] == 'Да':
                services.append('уход и лечение')

    return services

