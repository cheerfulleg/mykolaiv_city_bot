from aiogram import types

from config.settings import bot


async def send_to_users(telegram_ids: list, message: str, markup: types.InlineKeyboardMarkup = None):
    for user_id in telegram_ids:
        await bot.send_message(user_id, message, reply_markup=markup)