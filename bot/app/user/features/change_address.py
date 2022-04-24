import httpx
from aiogram import types
from aiogram.dispatcher import FSMContext

from app.user.markups import change_address, back, main_menu
from app.user.states import ChangeAddress
from config.settings import DOMAIN


async def show_change_address_keyboard(message: types.Message):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{DOMAIN}/user/{message.from_user.id}/address")

    await message.answer(f"Ваша адреса: {response.json().get('address')}", reply_markup=change_address())


async def request_change_address(message: types.Message):
    await ChangeAddress.address.set()
    await message.answer("Уведіть нову адресу", reply_markup=back())


async def process_change_address(message: types.Message, state: FSMContext):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{DOMAIN}/user/{message.from_user.id}/address", json={"address": message.text})

    if response.status_code == 200:
        await message.answer("Адресу змінено успішно", reply_markup=main_menu())
    else:
        await message.answer("Виникла помилка, спробуйте пізніше", reply_markup=main_menu())
    await state.finish()
