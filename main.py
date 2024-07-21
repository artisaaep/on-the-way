import asyncio
from telegram import form
from telegram.handlers import start
from telegram.bot_init import dp, bot
from telegram.callback_handlers import process_callback


async def main():
    dp.include_routers(
        start.router,
        form.router
    )
    print("Tg appearing...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
