from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text

from app.common.common_messages import cmd_start, cancel_handler


def register_common_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")
    dp.register_message_handler(cancel_handler, Text(equals="назад", ignore_case=True), state="*")
