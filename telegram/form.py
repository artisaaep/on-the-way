from random import random

from aiogram import Router
from aiogram import types
from bot_init import bot
from database import Database
from aiogram.types.web_app_info import WebAppInfo
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

router = Router()
db = Database("db.db")


class Form(StatesGroup):
    name = State()
    age = State()
    sex = State()
    bio = State()
    photo = State()
    finish = State()


@router.message(Form.name)
async def create(message: types.Message, state: FSMContext):
    await db.create_profile(message.from_user.id, alias=message.from_user.username)
    await message.answer("Укажи своё имя:", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Form.age)


@router.message(Form.age)
async def set_name(message: types.Message, state: FSMContext):
    await db.update_profile(user_id=message.from_user.id, name=message.text)
    await message.answer("Прекрасно, а теперь укажите ваш возраст\u263a\ufe0f", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Form.sex)


@router.message(Form.sex)
async def set_age(message: types.Message, state: FSMContext):
    try:
        await db.update_profile(user_id=message.from_user.id, age=int(message.text))
        markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Мужской")], [KeyboardButton(text="Женский")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
        )
        await message.answer("Укажите ваш пол", reply_markup=markup)
        await state.set_state(Form.bio)
    except:
        await message.answer("Введеный возраст некорректен, разрешены только цифры")
        await state.set_state(Form.sex)


@router.message(Form.bio)
async def set_sex(message: types.Message, state: FSMContext):
    if message.text == "Мужской":
        await db.update_profile(user_id=message.from_user.id, sex=0)
        await message.answer("Пришлите фото, которое будет отображаться в профиле",
                             reply_markup=ReplyKeyboardRemove())
        await state.set_state(Form.photo)
    elif message.text == "Женский":
        await db.update_profile(user_id=message.from_user.id, sex=1)
        await message.answer("Пришлите фото, которое будет отображаться в профиле",
                             reply_markup=ReplyKeyboardRemove())
        await state.set_state(Form.photo)
    else:
        await state.set_state(Form.bio)


@router.message(Form.photo)
async def set_photo(message: types.Message, state: FSMContext):
    if message.photo is not None:
        await bot.download(message.photo[-1], destination=f"photos/{message.from_user.id}.jpg")
        await message.answer("Ну и наполедок, напишите пару слов о себе, чтобы люди могли получше узнать вас\U0001f643",
                             reply_markup=ReplyKeyboardRemove())
        await state.set_state(Form.finish)
    else:
        await state.set_state(Form.photo)


@router.message(Form.finish)
async def set_bio(message: types.Message):
    await db.update_profile(user_id=message.from_user.id, bio=message.text)
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Создать поездку",
                            web_app=WebAppInfo(url="http://f0996151.xsph.ru"))], [
                KeyboardButton(text="Найти поездку",
                               web_app=WebAppInfo(url="http://f0996151.xsph.ru"))]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    await message.answer("Отлично!\U0001f973 Анкета создана, можете начать ваше чудесное путешествие\U0001f699",
                         reply_markup=markup)
