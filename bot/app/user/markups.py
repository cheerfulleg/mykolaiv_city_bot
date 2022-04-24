from aiogram import types


def back():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Назад")
    return markup


def district_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Центральний", "Заводський")
    markup.add("Інгульський", "Корабельний")
    return markup


def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Довідка", "Моя адреса")
    markup.add("Заявка", "Поділитися")
    return markup


def change_address():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Змінити адресу", "Назад")
    return markup


def share_inline():
    share_btn = types.InlineKeyboardButton("Поділитися", switch_inline_query="Awesome bot")
    return types.InlineKeyboardMarkup().add(share_btn)


def faq_inline():
    faq_btn_1 = types.InlineKeyboardButton("Один", callback_data="faq1")
    faq_btn_2 = types.InlineKeyboardButton("Два", callback_data="faq2")
    faq_btn_3 = types.InlineKeyboardButton("Три", callback_data="faq3")
    markup = types.InlineKeyboardMarkup(row_width=1)
    return markup.add(faq_btn_1, faq_btn_2, faq_btn_3)