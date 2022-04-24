from aiogram import types

from app.user.markups import faq_inline
from config.settings import bot


async def show_faq(message: types.Message):
    await message.answer("Довідка", reply_markup=faq_inline())


async def faq(callback_query: types.CallbackQuery):
    code = int(callback_query.data[-1])
    user_id = callback_query.from_user.id
    if code == 1:
        await bot.send_message(user_id, "Довідкова інфо про пункт 1")
    elif code == 2:
        await bot.send_message(user_id, "Довідкова інфо про пункт 2")
    elif code == 3:
        await bot.send_message(user_id, "Довідкова інфо про пункт 3")
