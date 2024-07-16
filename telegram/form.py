from pathlib import Path

from aiogram import Router
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

from shared.database_class import Database
from telegram.bot_init import bot
from telegram.config_reader import base_webapp_url
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()
db = Database()


class Form(StatesGroup):
    number = State()
    name = State()
    age = State()
    sex = State()
    photo = State()
    finish = State()


@router.message(Form.number)
async def num(message: types.Message, state: FSMContext):
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Предоставить данные", request_contact=True)]
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    await message.answer("Начинаем создание вашего профиля\nНажмите на кнопку ниже, чтобы предоставить ваш номер телефона", reply_markup=markup)
    await state.set_state(Form.name)

@router.message(Form.name)
async def create(message: types.Message, state: FSMContext):
    await state.update_data(number=f'+{message.contact.phone_number}')
    await message.answer("Теперь укажите Ваше имя и фамилию\U0001f607", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Form.age)


@router.message(Form.age)
async def set_name(message: types.Message, state: FSMContext):
    if len(message.text.split()) < 2:
        await message.answer("Вы не указали имя или фамилию, попробуйте ещё раз")
        await state.set_state(Form.age)
    else:
        await state.update_data(name=message.text)
        await message.answer("Прекрасно, а теперь укажите Ваш возраст\u263a\ufe0f", reply_markup=ReplyKeyboardRemove())
        await state.set_state(Form.sex)


@router.message(Form.sex)
async def set_age(message: types.Message, state: FSMContext):
    try:
        await state.update_data(age=int(message.text))
        markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Мужской")], [KeyboardButton(text="Женский")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
        )
        await message.answer("Укажите Ваш пол", reply_markup=markup)
        await state.set_state(Form.photo)
    except Exception:
        await message.answer("Введеный возраст некорректен, разрешены только цифры")
        await state.set_state(Form.sex)


@router.message(Form.photo)
async def set_sex(message: types.Message, state: FSMContext):
    if message.text != "Мужской" and message.text != "Женский":
        await state.set_state(Form.photo)
    elif message.text == "Мужской":
        await state.update_data(sex=0)
    elif message.text == "Женский":
        await state.update_data(sex=1)

    await message.answer("Теперь отправьте фото, которое будет отображаться в профиле",
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state(Form.finish)


@router.message(Form.finish)
async def set_photo(message: types.Message, state: FSMContext):
    if message.photo is None:
        await state.set_state(Form.finish)
        return
    data = await state.get_data()
    db.create_profile(
        user_id=message.from_user.id,
        alias=message.from_user.username,
        name=data['name'],
        age=data['age'],
        sex=data['sex'],
        number=data['number']
    )
    await bot.download(
        message.photo[-1],
        destination=Path(__file__).parent.parent / "shared" / "photos" / f"{message.from_user.id}.jpg"
    )

    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Создать поездку",
                                     web_app=WebAppInfo(url=base_webapp_url + "/app/createTrip.html")),
                InlineKeyboardButton(text="Найти поездку",
                                     web_app=WebAppInfo(url=base_webapp_url + "/app/availabletrips.html")))
    builder.row(InlineKeyboardButton(text="Мой профиль",
                                     web_app=WebAppInfo(url=base_webapp_url + "/app/profile.html")))
    await message.answer("Отлично!\U0001f973 Анкета создана, можете начать ваше чудесное путешествие\U0001f699",
                         reply_markup=builder.as_markup())
