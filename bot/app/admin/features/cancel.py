from aiogram import types
from aiogram.dispatcher import FSMContext

from app.admin.markups import admin_menu


async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Головне меню", reply_markup=admin_menu())