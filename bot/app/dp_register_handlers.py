from aiogram import Dispatcher

from app.admin.message_handler import register_admin_handlers
from app.common.register_common_handlers import register_common_handlers
from app.user.message_handler import register_user_handlers


def dp_register_handlers(dp: Dispatcher):
    register_common_handlers(dp)
    register_user_handlers(dp)
    register_admin_handlers(dp)
