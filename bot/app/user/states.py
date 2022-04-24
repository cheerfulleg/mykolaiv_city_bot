from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterForm(StatesGroup):
    first_name = State()
    last_name = State()
    phone = State()
    district = State()
    address = State()


class ChangeAddress(StatesGroup):
    address = State()


class ApplicationRequest(StatesGroup):
    application = State()
