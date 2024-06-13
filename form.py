from aiogram import Router
from aiogram.filters import CommandStart
from aiogram import types
from database import Database
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

router = Router()
db = Database("db.db")

@router.message()
async def create(message: types.Message):
    if message.text == "Начать регистрацию":
        await db.create_profile(message.from_user.id, "la", 12, 1, 1, "f")
