import httpx
from aiogram import types

from config.settings import DOMAIN


async def answer_poll(callback_query: types.CallbackQuery):
    answer = callback_query.data
    data = {
        "question": callback_query.message.text,
        "answer": answer,
        "telegram_id": callback_query.from_user.id
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{DOMAIN}/user/poll-answer", json=data)

    if response.status_code == 201:
        await callback_query.answer("Дякую за відповідь")
        await callback_query.message.delete()
    else:
        await callback_query.answer("Виникла помилка")
