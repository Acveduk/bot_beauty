from aiogram.dispatcher.filters.state import State, StatesGroup

from loader import dp


class Register_user(StatesGroup):
    City = State()
    phone_number = State()


class Vk(StatesGroup):
    vk_link = State()


class Insta(StatesGroup):
    insta_link = State()


class Telegram(StatesGroup):
    tg_link = State()


class City(StatesGroup):
    city_master = State()


class Address(StatesGroup):
    address_master = State()


class Fio(StatesGroup):
    fio_master = State()


class About_me(StatesGroup):
    about_me_master = State()


class Metro(StatesGroup):
    metro = State()


class Photo(StatesGroup):
    photo_master = State()


class Feedback_master(StatesGroup):
    master = State()
    star = State()
    feedback = State()
    recall = State()

class Feedback_client(StatesGroup):
    client = State()
    star = State()
    feedback = State()
    recall = State()

class Create(StatesGroup):
    city = State()
    metro = State()
    services = State()
    date_time = State()
    description = State()
    photo = State()


class Become_master(StatesGroup):
    profile = State()

class Reject(StatesGroup):
    profile = State()


class Purse(StatesGroup):
    sum = State()
    qiwi = State()
    ok = State()

class Donate(StatesGroup):
    sum = State()
    qiwi = State()
    ok = State()

class Question(StatesGroup):
    question = State()

class Answer(StatesGroup):
    answer = State()
    answer2 = State()

class Echo(StatesGroup):
    echo = State()


class Find_user(StatesGroup):
    user_id = State()

class Message_all_users(StatesGroup):
    message_users = State()