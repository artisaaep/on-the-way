import asyncio
from threading import Thread

from telegram import form
from telegram.handlers import start
from telegram.bot_init import dp, bot
from web.server import start as web_start


async def main():
    dp.include_routers(
        start.router,
        form.router
    )
    print("Tg appearing...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

