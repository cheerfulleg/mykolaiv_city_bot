import httpx
from aiogram import types
from aiogram.dispatcher import FSMContext

from app.common.markups import REMOVE_KEYBOARD
from app.user.markups import district_markup, main_menu
from app.user.states import RegisterForm
from config.settings import DOMAIN


async def process_first_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text

    await RegisterForm.next()
    await message.answer("Укажіть ваше прізвище")


async def process_last_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text

    await RegisterForm.next()
    await message.answer("Укажіть ваш номер телефону (у форматі 380981234567)")


# Check phone. Phone gotta be digit
async def process_phone_invalid(message: types.Message):
    return await message.answer("Укажіть номер телефону у правильному форматі")


async def process_phone(message: types.Message, state: FSMContext):
    await RegisterForm.next()
    await state.update_data(phone=int(message.text))
    await message.answer("У якому районі проживаєте?", reply_markup=district_markup())


async def process_district_invalid(message: types.Message):
    return await message.reply("Такого району не має у списку")


async def process_district(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["district"] = message.text.lower()

    await message.answer(
        "Укажіть свою адресу. Наприклад: вул. Архітектора Старова 10-Б",
        reply_markup=REMOVE_KEYBOARD,
    )

    await RegisterForm.next()


async def process_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["address"] = message.text
        data["telegram_id"] = message.from_user.id

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{DOMAIN}/user", json=data.as_dict())

    if response.status_code == 201:
        await message.answer('Реєстрація успішно завершена!', reply_markup=main_menu())

    elif response.status_code == 409:
        await message.answer('Ви вже зареєстровані!', reply_markup=main_menu())
    await state.finish()
