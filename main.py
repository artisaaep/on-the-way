import asyncio

import form
from config_reader import config
from aiogram import Bot, Dispatcher
from handlers import start

bot = Bot(token=config.bot_token.get_secret_value())

dp = Dispatcher()


async def main():
    dp.include_routers(
        start.router,
        form.router
    )
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
