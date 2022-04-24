from aiogram import types
import httpx
from aiogram.dispatcher import FSMContext

from app.admin.markups import admin_menu, cancel, choose_audience_markup, confirm_sending, choose_district_admin
from app.admin.states import Post
from app.admin.utils import send_to_users
from config.settings import DOMAIN, bot


async def start_post_creation(message: types.Message):
    await Post.content.set()
    await message.answer("Напишіть повідомлення", reply_markup=cancel())


async def enter_content(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["content"] = message.text

    await message.answer("Виберіть аудиторію отримувачів", reply_markup=choose_audience_markup())
    await Post.next()


async def choose_district_or_skip(message: types.Message):
    if message.text.lower() == "усі":
        await Post.confirm.set()
        await message.answer("Підтвердити відправку", reply_markup=confirm_sending())
    elif message.text.lower() == "за районом":
        await Post.district.set()
        await message.answer("Виберіть район", reply_markup=choose_district_admin())


async def choose_district_invalid(message: types.Message):
    return await message.reply("Такого району не має у списку")


# choose district state
async def choose_district(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["district"] = message.text
    await Post.next()

    await message.answer("Підтвердити відправку", reply_markup=confirm_sending())


async def send_post_to_users(data):
    telegram_ids = data["related_telegram_ids"]
    content = data["content"]
    for user_id in telegram_ids:
        await bot.send_message(user_id, content)


async def confirm_post(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["telegram_id"] = message.from_user.id

        async with httpx.AsyncClient() as client:
            response = await client.post(f"{DOMAIN}/admin/post?district={data.pop('district', '')}",
                                         json=data.as_dict())

    if response.status_code == 201:
        await message.answer("Повідомлення створено успішно", reply_markup=admin_menu())
    else:
        await message.answer("Сталася помилка, спробуйте ще раз", reply_markup=admin_menu())

    response_data = response.json()
    await send_to_users(response_data["related_telegram_ids"], response_data["content"])

    await state.finish()
