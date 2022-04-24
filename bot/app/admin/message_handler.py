from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text

from app.admin.features.cancel import cancel
from app.admin.features.create_poll import start_poll_creation, enter_question, enter_answers, confirm_poll
from app.admin.features.create_post import start_post_creation, enter_content, choose_district_or_skip, \
    choose_district_invalid, choose_district, confirm_post
from app.admin.features.login import login, logout
from app.admin.features.retrieve_applications import retrieve_applications
from app.admin.states import Post, Poll


def register_admin_handlers(dp: Dispatcher):
    # cancel
    dp.register_message_handler(cancel, commands="cancel", state="*")
    dp.register_message_handler(cancel, Text(equals="скасувати", ignore_case=True), state="*")
    # login
    dp.register_message_handler(login, commands="admin")
    dp.register_message_handler(logout, commands="exit", state="*")
    dp.register_message_handler(logout, Text(equals="вийти", ignore_case=True), state="*")
    # create post
    dp.register_message_handler(start_post_creation, Text(equals="створити пост", ignore_case=True))
    dp.register_message_handler(enter_content, state=Post.content)
    dp.register_message_handler(choose_district_or_skip, state=Post.audience)
    dp.register_message_handler(choose_district_invalid,
                                lambda message: message.text not in
                                                ["Центральний", "Заводський",
                                                 "Інгульський", "Корабельний", "Скасувати"],
                                state=Post.district)
    dp.register_message_handler(choose_district, state=Post.district)
    dp.register_message_handler(confirm_post, Text(equals="так", ignore_case=True), state=Post.confirm)
    # create poll
    dp.register_message_handler(start_poll_creation, Text(equals="створити опитування", ignore_case=True))
    dp.register_message_handler(enter_question, state=Poll.question)
    dp.register_message_handler(enter_answers, state=Poll.answers)
    dp.register_message_handler(confirm_poll, Text(equals="так", ignore_case=True), state=Poll.confirm)
    # Retrieve applications
    dp.register_message_handler(retrieve_applications, Text(equals="переглянути заявки", ignore_case=True))