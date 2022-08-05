from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from utils.db_api import postgres


class CheckUsers(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        if await postgres.check_user(user_id=message.from_user.id):
            return True
        else:
            return False

class CheckAdmin(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        if await postgres.check_admin_in_database(admin_id=message.from_user.id):
            return True
        else:
            return False

class CheckClient(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        sub = await postgres.get_sub_master(user_id=message.from_user.id)
        if sub[0]['manicure_pedicure'] == 'Пусто' or sub[0]['visage'] == 'Пусто' or sub[0][
            'other_services'] == 'Пусто' or sub[0]['hairdresser'] == 'Пусто':
            return True
        else:
            return False


class CheckMaster(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        sub = await postgres.get_sub_master(user_id=message.from_user.id)
        if sub[0]['manicure_pedicure'] != 'Пусто' and sub[0]['visage'] != 'Пусто' and sub[0][
            'other_services'] != 'Пусто' and sub[0]['hairdresser'] != 'Пусто':
            return True
        else:
            return False


class CheckVisage(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        sub = await postgres.get_sub_master(user_id=message.from_user.id)
        if sub[0]['visage'] == 'Да':
            return True
        else:
            return False


class CheckClientCall(BoundFilter):
    async def check(self, call: types.CallbackQuery) -> bool:
        sub = await postgres.get_sub_master(user_id=call.from_user.id)
        if sub[0]['manicure_pedicure'] == 'Пусто' or sub[0]['visage'] == 'Пусто' or sub[0][
            'other_services'] == 'Пусто' or sub[0]['hairdresser'] == 'Пусто':
            return True
        else:
            return False


class CheckMasterCall(BoundFilter):
    async def check(self, call: types.CallbackQuery) -> bool:
        sub = await postgres.get_sub_master(user_id=call.from_user.id)
        if sub[0]['manicure_pedicure'] != 'Пусто' or sub[0]['visage'] != 'Пусто' or sub[0][
            'other_services'] != 'Пусто' or sub[0]['hairdresser'] != 'Пусто':
            return True
        else:
            return False
