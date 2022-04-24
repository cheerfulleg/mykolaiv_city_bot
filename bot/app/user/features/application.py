import httpx
from aiogram import types
from aiogram.dispatcher import FSMContext

from app.user.markups import back, main_menu
from app.user.states import ApplicationRequest
from config.settings import DOMAIN


async def request_application(message: types.Message):
    await ApplicationRequest.application.set()
    await message.answer("Напишіть заявку", reply_markup=back())


async def process_application(message: types.Message, state: FSMContext):
    async with httpx.AsyncClient() as client:
        data = {"telegram_id": message.from_user.id, "content": message.text}
        response = await client.post(f"{DOMAIN}/user/application", json=data)

    if response.status_code == 201:
        await message.answer("Заявку надіслано успішно", reply_markup=main_menu())
    else:
        await message.answer("Виникла помилка, спробуйте пізніше", reply_markup=main_menu())
    await state.finish()
