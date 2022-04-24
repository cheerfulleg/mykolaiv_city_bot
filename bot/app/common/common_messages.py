from aiogram import types
from aiogram.dispatcher import FSMContext

from app.user.markups import main_menu
from app.user.states import RegisterForm
from config.settings import bot, logger


async def cmd_start(message: types.Message):
    await RegisterForm.first_name.set()
    await bot.send_message(message.chat.id, "Вітаю, я Сіті бот! Укажіть ваше ім'я:")


async def cancel_handler(message: types.Message, state: FSMContext):
    if current_state := await state.get_state() is not None:
        await state.finish()
    await message.answer("Головне меню", reply_markup=main_menu())

    logger.info('Cancelling state %r', current_state)


