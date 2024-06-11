from aiogram import Router
from aiogram.filters import CommandStart
from aiogram import types
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет!")
