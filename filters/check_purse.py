from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from utils.db_api import postgres


class PurseClient(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        purse = await postgres.purse(user_id=message.from_user.id)
        if int(purse[0]['purse']) < 0:
            return True
        else:
            return False

class PurseMaster(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        purse = await postgres.purse(user_id=message.from_user.id)
        if int(purse[0]['purse']) >= 0:
            return True
        else:
            return False