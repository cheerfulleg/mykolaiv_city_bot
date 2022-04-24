from aiogram import types

from app.user.markups import share_inline
from config.settings import bot


async def share_bot(message: types.Message):
    await message.answer("Поділіться ботом зі своїми контактами", reply_markup=share_inline())
