from aiogram.dispatcher.filters.state import StatesGroup, State


class Post(StatesGroup):
    content = State()
    audience = State()
    district = State()
    confirm = State()


class Poll(StatesGroup):
    question = State()
    answers = State()
    confirm = State()
