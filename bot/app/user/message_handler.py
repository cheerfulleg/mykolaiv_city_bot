from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text

from app.user.features.answer_poll import answer_poll
from app.user.features.application import request_application, process_application
from app.user.features.change_address import show_change_address_keyboard, request_change_address, \
    process_change_address
from app.user.features.faq import show_faq, faq
from app.user.features.registration import process_first_name, process_last_name, process_phone_invalid, \
    process_phone, process_district_invalid, process_district, process_address
from app.user.features.share import share_bot
from app.user.states import RegisterForm, ChangeAddress, ApplicationRequest


def register_user_handlers(dp: Dispatcher):
    # register
    dp.register_message_handler(process_first_name, state=RegisterForm.first_name)
    dp.register_message_handler(process_last_name, state=RegisterForm.last_name)
    dp.register_message_handler(process_phone_invalid,
                                lambda message: not message.text.isdigit() or len(message.text) != 12,
                                state=RegisterForm.phone)
    dp.register_message_handler(process_phone, lambda message: message.text.isdigit() and len(message.text) == 12,
                                state=RegisterForm.phone)
    dp.register_message_handler(process_district_invalid,
                                lambda message: message.text not in
                                                ["Центральний", "Заводський", "Інгульський", "Корабельний"],
                                state=RegisterForm.district)
    dp.register_message_handler(process_district, state=RegisterForm.district)
    dp.register_message_handler(process_address, state=RegisterForm.address)
    # change_address
    dp.register_message_handler(show_change_address_keyboard, Text(equals="моя адреса", ignore_case=True))
    dp.register_message_handler(request_change_address, Text(equals="змінити адресу", ignore_case=True))
    dp.register_message_handler(process_change_address, state=ChangeAddress.address)
    # application
    dp.register_message_handler(request_application, Text(equals="заявка", ignore_case=True))
    dp.register_message_handler(process_application, state=ApplicationRequest.application)
    # share
    dp.register_message_handler(share_bot, Text(equals="поділитися", ignore_case=True))
    # faq
    dp.register_message_handler(show_faq, Text(equals="довідка", ignore_case=True))
    dp.register_callback_query_handler(faq, lambda c: c.data and c.data.startswith('faq'))
    # Answer poll
    dp.register_callback_query_handler(answer_poll)

