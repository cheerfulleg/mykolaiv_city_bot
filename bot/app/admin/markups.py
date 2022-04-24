from aiogram import types


def admin_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Створити пост", "Створити опитування")
    markup.add("Переглянути заявки", "Вийти")
    return markup


def cancel():
    return types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add("Скасувати")


def choose_audience_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Усі", "За районом")
    markup.add("Скасувати")
    return markup


def choose_district_admin():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Центральний", "Заводський")
    markup.add("Інгульський", "Корабельний")
    markup.add("Скасувати")
    return markup


def confirm_sending():
    return types.ReplyKeyboardMarkup().add("Так", "Скасувати")


def generate_inline_poll_markup(answers):
    markup = types.InlineKeyboardMarkup(row_width=1, one_time_keyboard=True)
    for answer in answers:
        markup.add(types.InlineKeyboardButton(answer, callback_data=answer))

    return markup
