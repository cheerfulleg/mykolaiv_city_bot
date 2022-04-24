import asyncio

from app.dp_register_handlers import dp_register_handlers
from config.settings import dp


async def main():
    dp_register_handlers(dp)
    await dp.skip_updates()
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
