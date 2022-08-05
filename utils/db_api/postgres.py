import asyncpg


async def check_admin_in_database(admin_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT 1 FROM admin_users WHERE admin_id = $1'

    select = await connect.fetch(sql_command, admin_id)
    await connect.close()

    return len(select)


async def update_master(user_id: int, purse: int, manicure_pedicure: str, hairdresser: str, visage: str,
                        other_services: str, favorites: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE user_bot SET purse = $1, manicure_pedicure = $2, hairdresser = $3, visage = $4, other_services = $5, favorites = $6 WHERE user_id = $7'

    await connect.execute(sql_command, purse, manicure_pedicure, hairdresser, visage, other_services, favorites,
                          user_id)
    await connect.close()


async def add_user_in_database(user_id: int, name_user: str, phone_number: int, fio: str, photo: str,
                               city: str, metro: str, address: str, insta: str, vk: str, telegram: str,
                               about_me: str, purse: int, manicure_pedicure: str, hairdresser: str, visage: str,
                               other_services: str, favorites: int,
                               date_reg):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'INSERT INTO user_bot(user_id, name_user, phone_number, fio, photo, city, metro, address, insta, vk, telegram, about_me, purse, manicure_pedicure, hairdresser, visage, other_services, favorites, date_reg) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19)'

    await connect.execute(sql_command, user_id, name_user, phone_number, fio, photo, city, metro, address, insta, vk,
                          telegram, about_me, purse, manicure_pedicure, hairdresser, visage, other_services, favorites,
                          date_reg)
    await connect.close()


async def check_user(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT 1 FROM user_bot WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return len(select)


async def check_user_in_database(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT 1 FROM master WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return len(select)


async def get_user(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT * FROM user_bot WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def get_client(user_number: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT * FROM user_bot WHERE user_number = $1'

    select = await connect.fetch(sql_command, user_number)
    await connect.close()

    return select


async def update_vk(user_id: int, vk: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE user_bot SET vk = $1 WHERE user_id = $2'

    await connect.execute(sql_command, vk, user_id)
    await connect.close()


async def update_insta(user_id: int, insta: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE user_bot SET insta = $1 WHERE user_id = $2'

    await connect.execute(sql_command, insta, user_id)
    await connect.close()


async def update_tg(user_id: int, telegram: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE user_bot SET telegram = $1 WHERE user_id = $2'

    await connect.execute(sql_command, telegram, user_id)
    await connect.close()


async def update_city(user_id: int, city: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE user_bot SET city = $1 WHERE user_id = $2'

    await connect.execute(sql_command, city, user_id)
    await connect.close()


async def update_metro(user_id: int, metro: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE user_bot SET metro = $1 WHERE user_id = $2'

    await connect.execute(sql_command, metro, user_id)
    await connect.close()


async def update_photo(user_id: int, photo: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE user_bot SET photo = $1 WHERE user_id = $2'

    await connect.execute(sql_command, photo, user_id)
    await connect.close()


async def update_address(user_id: int, address: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE user_bot SET address = $1 WHERE user_id = $2'

    await connect.execute(sql_command, address, user_id)
    await connect.close()


async def update_fio(user_id: int, fio: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE user_bot SET fio = $1 WHERE user_id = $2'

    await connect.execute(sql_command, fio, user_id)
    await connect.close()


async def update_about_me(user_id: int, about_me: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE user_bot SET about_me = $1 WHERE user_id = $2'

    await connect.execute(sql_command, about_me, user_id)
    await connect.close()


async def check_master_in_manicure(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT 1 FROM manicure_pedicure WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return len(select)


async def check_master_in_visage(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT 1 FROM visage WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return len(select)


async def check_master_in_hairdresser(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT 1 FROM hairdresser WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return len(select)


async def check_master_in_other_services(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT 1 FROM other_services WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return len(select)


async def add_master_in_manicure(user_id: int, manicure: str, pedicure: str, date_start, date_end):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'INSERT INTO manicure_pedicure(user_id, manicure, pedicure, date_start, date_end) VALUES ($1, $2, $3, $4, $5)'

    await connect.execute(sql_command, user_id, manicure, pedicure, date_start, date_end)
    await connect.close()


async def add_master_in_visage(user_id: int, makeup: str, eyebrows: str, eyelashes: str, wedding_image: str, date_start,
                               date_end):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'INSERT INTO visage(user_id, makeup, eyebrows, eyelashes, wedding_image, date_start, date_end) VALUES ($1, $2, $3, $4, $5, $6, $7)'

    await connect.execute(sql_command, user_id, makeup, eyebrows, eyelashes, wedding_image, date_start, date_end)
    await connect.close()


async def add_master_in_hairdresser(user_id: int, haircut: str, man_haircut: str, hair_styling: str, hair_coloring: str,
                                    hair_care: str, date_start, date_end):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'INSERT INTO hairdresser(user_id, haircut, man_haircut, hair_styling, hair_coloring, hair_care, date_start, date_end) VALUES ($1, $2, $3, $4, $5, $6, $7, $8)'

    await connect.execute(sql_command, user_id, haircut, man_haircut, hair_styling, hair_coloring, hair_care,
                          date_start, date_end)
    await connect.close()


async def add_master_in_other(user_id: int, massage: str, depilation_with_wax: str, shugaring: str, date_start,
                              tan_at_home: str,
                              date_end):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'INSERT INTO other_services(user_id, massage, depilation_with_wax, shugaring, date_start, date_end, tan_at_home) VALUES ($1, $2, $3, $4, $5, $6, $7)'

    await connect.execute(sql_command, user_id, massage, depilation_with_wax, shugaring, date_start, date_end,
                          tan_at_home)
    await connect.close()


async def check_manicure(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT manicure, pedicure FROM manicure_pedicure WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def check_other_services(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT massage, depilation_with_wax, shugaring, tan_at_home FROM other_services WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def check_visage(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT makeup, eyebrows, eyelashes, wedding_image FROM visage WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def check_hairdresser(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT haircut, man_haircut, hair_styling, hair_coloring, hair_care FROM hairdresser WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def select_city(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT city FROM user_bot WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def update_manicure(user_id: int, manicure: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE manicure_pedicure SET manicure = $1 WHERE user_id = $2'

    await connect.execute(sql_command, manicure, user_id)
    await connect.close()


async def update_makeup(user_id: int, makeup: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE visage SET makeup = $1 WHERE user_id = $2'

    await connect.execute(sql_command, makeup, user_id)
    await connect.close()


async def update_haircut(user_id: int, haircut: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE hairdresser SET haircut = $1 WHERE user_id = $2'

    await connect.execute(sql_command, haircut, user_id)
    await connect.close()


async def update_man_haircut(user_id: int, man_haircut: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE hairdresser SET man_haircut = $1 WHERE user_id = $2'

    await connect.execute(sql_command, man_haircut, user_id)
    await connect.close()


async def update_hair_styling(user_id: int, hair_styling: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE hairdresser SET hair_styling = $1 WHERE user_id = $2'

    await connect.execute(sql_command, hair_styling, user_id)
    await connect.close()


async def update_hair_coloring(user_id: int, hair_coloring: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE hairdresser SET hair_coloring = $1 WHERE user_id = $2'

    await connect.execute(sql_command, hair_coloring, user_id)
    await connect.close()


async def update_hair_care(user_id: int, hair_care: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE hairdresser SET hair_care = $1 WHERE user_id = $2'

    await connect.execute(sql_command, hair_care, user_id)
    await connect.close()


async def update_eyebrows(user_id: int, eyebrows: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE visage SET eyebrows = $1 WHERE user_id = $2'

    await connect.execute(sql_command, eyebrows, user_id)
    await connect.close()


async def update_eyelashes(user_id: int, eyelashes: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE visage SET eyelashes = $1 WHERE user_id = $2'

    await connect.execute(sql_command, eyelashes, user_id)
    await connect.close()


async def update_wedding_image(user_id: int, wedding_image: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE visage SET wedding_image = $1 WHERE user_id = $2'

    await connect.execute(sql_command, wedding_image, user_id)
    await connect.close()


async def update_massage(user_id: int, massage: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE other_services SET massage = $1 WHERE user_id = $2'

    await connect.execute(sql_command, massage, user_id)
    await connect.close()


async def update_depilation_with_wax(user_id: int, depilation_with_wax: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE other_services SET depilation_with_wax = $1 WHERE user_id = $2'

    await connect.execute(sql_command, depilation_with_wax, user_id)
    await connect.close()


async def update_shugaring(user_id: int, shugaring: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE other_services SET shugaring = $1 WHERE user_id = $2'

    await connect.execute(sql_command, shugaring, user_id)
    await connect.close()


async def update_tan_at_home(user_id: int, tan_at_home: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE other_services SET tan_at_home = $1 WHERE user_id = $2'

    await connect.execute(sql_command, tan_at_home, user_id)
    await connect.close()


async def update_pedicure(user_id: int, pedicure: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE manicure_pedicure SET pedicure = $1 WHERE user_id = $2'

    await connect.execute(sql_command, pedicure, user_id)
    await connect.close()


async def get_manicure(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT manicure, pedicure FROM manicure_pedicure WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def check_date_sub_hairdresser(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT date_end FROM hairdresser WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def check_date_sub_manicure_pedicure(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT date_end FROM manicure_pedicure WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def check_date_sub_visage(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT date_end FROM visage WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def check_date_sub_other_services(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT date_end FROM other_services WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def get_sub_master(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT manicure_pedicure, other_services, visage, hairdresser FROM user_bot WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def update_sub_manicure(user_id: int, manicure_pedicure: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE user_bot SET manicure_pedicure = $1 WHERE user_id = $2'

    await connect.execute(sql_command, manicure_pedicure, user_id)
    await connect.close()


async def update_sub_hairdresser(user_id: int, hairdresser: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE user_bot SET hairdresser = $1 WHERE user_id = $2'

    await connect.execute(sql_command, hairdresser, user_id)
    await connect.close()


async def update_sub_visage(user_id: int, visage: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE user_bot SET visage = $1 WHERE user_id = $2'

    await connect.execute(sql_command, visage, user_id)
    await connect.close()


async def update_sub_other_services(user_id: int, other_services: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE user_bot SET other_services = $1 WHERE user_id = $2'

    await connect.execute(sql_command, other_services, user_id)
    await connect.close()


async def subscribe(user_id: int, purse: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE user_bot SET purse = $1 WHERE user_id = $2'

    await connect.execute(sql_command, purse, user_id)
    await connect.close()


async def purse(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT purse FROM user_bot WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def update_date_sub_manicure(user_id: int, date_start, date_end):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE manicure_pedicure SET date_start = $1, date_end = $2 WHERE user_id = $3'

    await connect.execute(sql_command, date_start, date_end, user_id)
    await connect.close()


async def update_date_sub_hairdresser(user_id: int, date_start, date_end):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE hairdresser SET date_start = $1, date_end = $2 WHERE user_id = $3'

    await connect.execute(sql_command, date_start, date_end, user_id)
    await connect.close()


async def update_date_sub_visage(user_id: int, date_start, date_end):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE visage SET date_start = $1, date_end = $2 WHERE user_id = $3'

    await connect.execute(sql_command, date_start, date_end, user_id)
    await connect.close()


async def update_date_sub_other_services(user_id: int, date_start, date_end):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE other_services SET date_start = $1, date_end = $2 WHERE user_id = $3'

    await connect.execute(sql_command, date_start, date_end, user_id)
    await connect.close()


async def check_master_in_recall(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT 1 FROM recall_master WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return len(select)


async def get_rating(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT rating_up, rating_down FROM master WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def get_last_recall_master(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT recall, name_recall FROM recall_master WHERE user_id = $1 ORDER BY number_recall DESC LIMIT(5)'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def get_last_recall_client(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT recall, name_recall FROM recall_client WHERE user_id = $1 ORDER BY number_recall DESC LIMIT(5)'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def select_all_client_user_number(text: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')
    if text == '№:':
        text += ''
    elif text == "Никнейм:":
        text += ''
    elif text == '':
        text += ''
    number = text.split(":")[-1]
    print(number)
    if text == f"№:{number}":
        q = f"'%{str(number)}%'"
        sql_command = f"""
        SELECT * FROM user_bot WHERE (visage != 'Пусто' AND hairdresser != 'Пусто' AND manicure_pedicure != 'Пусто' AND other_services != 'Пусто') AND CAST(user_number as text) LIKE 
        """ + q
        select = await connect.fetch(sql_command)
        await connect.close()
        return select

    elif text == f"Никнейм:{number}":
        q = f"'%{str(number)}%'"
        sql_command = f"""
            SELECT * FROM user_bot WHERE (visage != 'Пусто' AND hairdresser != 'Пусто' AND manicure_pedicure != 'Пусто' AND other_services != 'Пусто') AND name_user LIKE 
            """ + q
        select = await connect.fetch(sql_command)
        await connect.close()

        return select

    else:
        q = f"'%{str(number)}%'"
        sql_command = f"""
                    SELECT * FROM user_bot WHERE (visage != 'Пусто' AND hairdresser != 'Пусто' AND manicure_pedicure != 'Пусто' AND other_services != 'Пусто') AND name_user LIKE 
                    """ + q
        select = await connect.fetch(sql_command)
        await connect.close()

        return select


async def select_all_user_user_number(text: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')
    if text == '№:':
        text += ''
    elif text == 'Телефон:':
        text += ''
    elif text == "Никнейм:":
        text += ''
    elif text == '':
        text += ''
    number = text.split(":")[-1]
    print(number)
    if text == f"№:{number}":
        q = f"'%{str(number)}%'"
        sql_command = f"""
        SELECT * FROM user_bot WHERE CAST(user_number as text) LIKE 
        """ + q
        select = await connect.fetch(sql_command)
        await connect.close()
        return select

    elif text == f"Телефон:{number}":
        q = f"'%{str(number)}%'"
        sql_command = f"""
            SELECT * FROM user_bot WHERE CAST(phone_number as text) LIKE 
            """ + q
        select = await connect.fetch(sql_command)
        await connect.close()

        return select

    elif text == f"Никнейм:{number}":
        q = f"'%{str(number)}%'"
        sql_command = f"""
            SELECT * FROM user_bot WHERE name_user LIKE 
            """ + q
        select = await connect.fetch(sql_command)
        await connect.close()

        return select

    else:
        q = f"'%{str(number)}%'"
        sql_command = f"""
                    SELECT * FROM user_bot WHERE name_user LIKE 
                    """ + q
        select = await connect.fetch(sql_command)
        await connect.close()

        return select


async def get_master(user_number: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT * FROM user_bot WHERE user_number = $1'

    select = await connect.fetch(sql_command, user_number)
    await connect.close()

    return select


async def check_rating(user_id: int, id_evaluating: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT 1 FROM rating_client WHERE user_id = $1 AND id_evaluating = $2'

    select = await connect.fetch(sql_command, user_id, id_evaluating)
    await connect.close()

    return len(select)


async def check_rating_client(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT 1 FROM rating_client WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return len(select)


async def check_rating_master(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT 1 FROM rating_master WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return len(select)


async def check_ban(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT 1 FROM ban WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return len(select)


async def rating_client(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT rating_up, rating_down FROM client WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def add_rating_client(user_id: int, id_evaluating: int, rating: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'INSERT INTO rating_client(user_id, id_evaluating, rating) VALUES ($1, $2, $3)'

    await connect.execute(sql_command, user_id, id_evaluating, rating)
    await connect.close()


async def add_rating_master(user_id: int, client_id: int, rating: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'INSERT INTO rating_master(user_id, client_id, rating) VALUES ($1, $2, $3)'

    await connect.execute(sql_command, user_id, client_id, rating)
    await connect.close()


async def add_rating_chek(user_id: int, id_evaluating: int, rating: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'INSERT INTO client(id_evaluating, rating user_id) VALUES ($1, $2, $3)'

    await connect.execute(sql_command, id_evaluating, rating, user_id)
    await connect.close()


async def check_recall_client(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT 1 FROM recall_client WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return len(select)


async def add_recall_client(user_id: int, recall: str, name_recall: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'INSERT INTO recall_client(user_id, recall, name_recall) VALUES ($1, $2, $3)'

    await connect.execute(sql_command, user_id, recall, name_recall)
    await connect.close()


async def check_recall_master(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT 1 FROM recall_master WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return len(select)


async def add_recall_master(user_id: int, recall: str, name_recall: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'INSERT INTO recall_master(user_id, recall, name_recall) VALUES ($1, $2, $3)'

    await connect.execute(sql_command, user_id, recall, name_recall)
    await connect.close()


async def select_rating_master(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT AVG(rating) FROM rating_master WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def select_rating_client(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT AVG(rating) FROM rating_client WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def add_applications(user_id: int, city: str, metro: str, service: str, date_time: str, description: str,
                           photo: str, name: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'INSERT INTO applications(user_id, city, metro, service, date_time, description, photo, name) VALUES ($1, $2, $3, $4, $5, $6, $7, $8)'

    await connect.execute(sql_command, user_id, city, metro, service, date_time, description, photo, name)
    await connect.close()


async def select_number_applications(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT MAX(number_applications) FROM applications WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def select_photo(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT photo FROM applications WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def select_top_master_manicure(city: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f"SELECT user_bot.user_id, user_bot.name_user, user_bot.user_number, AVG(rating), (COUNT(rating_master.user_id) >= 3) AS BEST FROM user_bot INNER JOIN rating_master ON user_bot.user_id = rating_master.user_id WHERE manicure_pedicure = 'Да' AND city = $1 GROUP BY user_bot.user_id ORDER BY avg DESC"

    select = await connect.fetch(sql_command, city)
    await connect.close()

    return select


async def select_top_master_hairdresser(city: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f"SELECT user_bot.user_id, user_bot.name_user, user_bot.user_number, AVG(rating), (COUNT(rating_master.user_id) >= 3) AS BEST FROM user_bot INNER JOIN rating_master ON user_bot.user_id = rating_master.user_id WHERE hairdresser = 'Да' AND city = $1 GROUP BY user_bot.user_id ORDER BY avg DESC"

    select = await connect.fetch(sql_command, city)
    await connect.close()

    return select


async def select_top_master_visage(city: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f"SELECT user_bot.user_id, user_bot.name_user, user_bot.user_number, AVG(rating), (COUNT(rating_master.user_id) >= 3) AS BEST FROM user_bot INNER JOIN rating_master ON user_bot.user_id = rating_master.user_id WHERE visage = 'Да' AND city = $1 GROUP BY user_bot.user_id ORDER BY avg DESC"

    select = await connect.fetch(sql_command, city)
    await connect.close()

    return select


async def select_top_master_other_services(city: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f"SELECT user_bot.user_id, user_bot.name_user, user_bot.user_number, AVG(rating), (COUNT(rating_master.user_id) >= 3) AS BEST FROM user_bot INNER JOIN rating_master ON user_bot.user_id = rating_master.user_id WHERE other_services = 'Да' AND city = $1 GROUP BY user_bot.user_id ORDER BY avg DESC"

    select = await connect.fetch(sql_command, city)
    await connect.close()

    return select


async def top_rating():
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f"SELECT user_id, AVG(rating), (COUNT(user_id) >= 3) AS BEST FROM rating_master GROUP BY user_id ORDER BY avg DESC"

    select = await connect.fetch(sql_command)
    await connect.close()

    return select


async def add_master_in_favorites(user_id: int, master_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'INSERT INTO favorites(user_id, master_id) VALUES ($1, $2)'

    await connect.execute(sql_command, user_id, master_id)
    await connect.close()


async def select_master_in_favorites(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT master_id FROM favorites WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def delete_master_in_favorites(user_id: int, master_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'DELETE FROM favorites WHERE user_id = $1 AND master_id = $2'

    await connect.execute(sql_command, user_id, master_id)
    await connect.close()


async def check_user_in_favorites(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT 1 FROM favorites WHERE user_id = $1'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return len(select)


async def select_number_applications_favorites(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT number_applications, service FROM applications WHERE user_id = $1 ORDER BY number_applications DESC LIMIT(5)'

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def update_purse_master(user_id: int, purse: int, pay_id: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE user_bot SET purse = $1, pay_id = $2 WHERE user_id = $3'

    await connect.execute(sql_command, purse, pay_id, user_id)
    await connect.close()


async def update_donate(user_id: int, pay_id: str):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'UPDATE user_bot SET pay_id = $1 WHERE user_id = $2'

    await connect.execute(sql_command, pay_id, user_id)
    await connect.close()


async def delete_user(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f"DELETE FROM user_bot WHERE user_id=$1"

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def unblock_user(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f"DELETE FROM ban WHERE user_id=$1"

    select = await connect.fetch(sql_command, user_id)
    await connect.close()

    return select


async def ban_user(user_id: int):
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'INSERT INTO ban(user_id) VALUES ($1)'

    await connect.execute(sql_command, user_id)
    await connect.close()


async def get_all_users():
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT user_id FROM user_bot'

    select = await connect.fetch(sql_command)
    await connect.close()

    return select

async def get_all_info_users():
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT * FROM user_bot'

    select = await connect.fetch(sql_command)
    await connect.close()

    return select


async def count_users():
    connect = await asyncpg.connect(database='beauty', user='postgres',
                                    password='VLADIk1133')

    sql_command = f'SELECT COUNT(*) FROM user_bot'

    select = await connect.fetch(sql_command)
    await connect.close()

    return select
