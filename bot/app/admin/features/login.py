from aiogram import types
import httpx

from app.admin.markups import admin_menu
from app.user.markups import main_menu
from config.settings import DOMAIN


async def login(message: types.Message):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{DOMAIN}/admin/check/{message.from_user.id}")

    if response.status_code == 200:
        await message.answer("Ви увійшли до адмін панелі", reply_markup=admin_menu())


async def logout(message: types.Message):
    await message.answer("Ви вийшли з адмін панелі", reply_markup=main_menu())
