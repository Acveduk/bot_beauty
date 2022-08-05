from datetime import datetime, timedelta

from utils.db_api import postgres


async def prolong_sub(user_id):
    master = await postgres.get_user(user_id=user_id)
    if master[0]['manicure_pedicure'] != 'Пусто' and master[0]['visage'] != 'Пусто' and master[0][
        'other_services'] != 'Пусто' and master[0]['hairdresser'] != 'Пусто':
        if (master[0]['purse'] - 100) >= 0:
            if master[0]['manicure_pedicure'] == 'Да':
                if await postgres.check_master_in_manicure(user_id=user_id):
                    check_date_subscription = await postgres.check_date_sub_manicure_pedicure(user_id=user_id)
                    for check_date in check_date_subscription:
                        if datetime.now() > check_date['date_end']:
                            purse = master[0]['purse'] - 100
                            date_start = datetime.now()
                            date_end = date_start + timedelta(days=30)
                            await postgres.subscribe(user_id=user_id, purse=purse)
                            await postgres.update_date_sub_manicure(user_id=user_id, date_start=date_start,
                                                                    date_end=date_end)

            if master[0]['hairdresser'] == 'Да':
                if await postgres.check_master_in_hairdresser(user_id=user_id):
                    check_date_subscription = await postgres.check_date_sub_hairdresser(user_id=user_id)
                    for check_date in check_date_subscription:
                        if datetime.now() > check_date['date_end']:
                            purse = master[0]['purse'] - 100
                            date_start = datetime.now()
                            date_end = date_start + timedelta(days=30)
                            await postgres.subscribe(user_id=user_id, purse=purse)
                            await postgres.update_date_sub_hairdresser(user_id=user_id, date_start=date_start,
                                                                       date_end=date_end)

            if master[0]['visage'] == 'Да':
                if await postgres.check_master_in_visage(user_id=user_id):
                    check_date_subscription = await postgres.check_date_sub_visage(user_id=user_id)
                    for check_date in check_date_subscription:
                        if datetime.now() > check_date['date_end']:
                            purse = master[0]['purse'] - 100
                            date_start = datetime.now()
                            date_end = date_start + timedelta(days=30)
                            await postgres.subscribe(user_id=user_id, purse=purse)
                            await postgres.update_date_sub_visage(user_id=user_id, date_start=date_start,
                                                                  date_end=date_end)

            if master[0]['other_services'] == 'Да':
                if await postgres.check_master_in_other_services(user_id=user_id):
                    check_date_subscription = await postgres.check_date_sub_other_services(user_id=user_id)
                    for check_date in check_date_subscription:
                        if datetime.now() > check_date['date_end']:
                            purse = master[0]['purse'] - 100
                            date_start = datetime.now()
                            date_end = date_start + timedelta(days=30)
                            await postgres.subscribe(user_id=user_id, purse=purse)
                            await postgres.update_date_sub_other_services(user_id=user_id, date_start=date_start,
                                                                          date_end=date_end)
