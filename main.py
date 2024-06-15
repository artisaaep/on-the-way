import asyncio

import form
from handlers import start
from bot_init import dp, bot


async def main():
    dp.include_routers(
        start.router,
        form.router
    )
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
