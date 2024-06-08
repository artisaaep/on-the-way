from config_reader import config
from aiogram import Bot, Dispatcher, types
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters import CommandStart

bot = Bot(token=config.bot_token.get_secret_value())

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    markup = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(web_app=WebAppInfo(url="https://vk.com"))]]
    )
    await message.answer("Привет!", reply_markup=markup)




if __name__ == "__main__":
    dp.start_polling(bot)


