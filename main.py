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
    def __start():
        asyncio.run(main())
    web_thread = Thread(target=web_start)
    tg_thread = Thread(target=__start)
    web_thread.start()
    tg_thread.start()
    web_thread.join()
    tg_thread.join()
