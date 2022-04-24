import httpx
from aiogram import types
from aiogram.dispatcher import FSMContext

from app.admin.markups import admin_menu, cancel, confirm_sending, generate_inline_poll_markup
from app.admin.states import Poll
from app.admin.utils import send_to_users
from config.settings import DOMAIN, bot


async def start_poll_creation(message: types.Message):
    await Poll.question.set()
    await message.answer("Уведіть питання опитування", reply_markup=cancel())


async def enter_question(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["question"] = message.text

    await message.answer("Уведіть варіанти відповідей. Кожен варіант з нового рядка")
    await Poll.next()


async def enter_answers(message: types.Message, state: FSMContext):
    answers = message.text.split(sep='\n')
    async with state.proxy() as data:
        data["answers"] = answers

    await message.answer("Підтвердити відправку", reply_markup=confirm_sending())
    await Poll.next()


async def confirm_poll(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["telegram_id"] = message.from_user.id

        async with httpx.AsyncClient() as client:
            response = await client.post(f"{DOMAIN}/admin/poll", json=data.as_dict())

    if response.status_code == 201:
        await message.answer("Опитування створено успішно", reply_markup=admin_menu())
    else:
        await message.answer("Сталася помилка, спробуйте ще раз", reply_markup=admin_menu())

    response_data = response.json()
    markup = generate_inline_poll_markup(response_data["answers"])
    await send_to_users(response_data["related_telegram_ids"], response_data["question"], markup)

    await state.finish()
