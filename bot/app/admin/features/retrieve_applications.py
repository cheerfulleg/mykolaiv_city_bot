from aiogram import types
import httpx

from config.settings import DOMAIN


async def retrieve_applications(message: types.Message):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{DOMAIN}/admin/applications")

    if response.status_code == 200:
        response_data = response.json()
        for app in response_data:
            await message.answer(app["content"])
    else:
        await message.answer("Сталася помилка, спробуйте ще раз")