from aiogram import Dispatcher

from .check_user import CheckUsers, CheckMaster, CheckClient, CheckVisage, CheckClientCall, CheckMasterCall, CheckAdmin
from .check_purse import PurseClient, PurseMaster


def setup(dp: Dispatcher):
    dp.filters_factory.bind(CheckUsers)
    dp.filters_factory.bind(PurseClient)
    dp.filters_factory.bind(PurseMaster)
    dp.filters_factory.bind(CheckMaster)
    dp.filters_factory.bind(CheckClient)
    dp.filters_factory.bind(CheckVisage)
    dp.filters_factory.bind(CheckClientCall)
    dp.filters_factory.bind(CheckMasterCall)
    dp.filters_factory.bind(CheckAdmin)
