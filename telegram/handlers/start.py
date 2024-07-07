from aiogram import Router
from aiogram.filters import CommandStart
from aiogram import types
from shared.database_class import Database
from ..config_reader import base_webapp_url
from ..form import Form
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

router = Router()

db = Database()


@router.message(CommandStart())
async def start(message: types.Message, state: FSMContext):
    user_exists = db.exists(message.from_user.id)
    if not user_exists:
        text = "Привет!\n\nЭто сервис по поиску попутчиков <b>on the way</b> \U0001F699. \
Здесь вы можете найти с кем добраться до пункта назначения или создать поездку как водитель и найти пассажиров. \
Чтобы начать работу, необходимо зарегистрироваться. <b>Нажмите на кнопку ниже, чтобы начать регистрацию</b>."
        markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Начать регистрацию")],
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
        )
        await state.set_state(Form.name)
        await message.answer(text, reply_markup=markup, parse_mode='html')
    else:
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Создать поездку",
                                         web_app=WebAppInfo(url=base_webapp_url + "/static/createtrip.html")),
                    InlineKeyboardButton(text="Найти поездку",
                                         web_app=WebAppInfo(url=base_webapp_url + "/static/availabletrips.html")),
                ],
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
        )
        text = "Привет!\n\nЭто сервис по поиску попутчиков <b>on the way</b>. \
Здесь вы можете найти с кем добраться до пункта назначения или создать поездку как водитель и найти пассажиров. \U0001F699 "
        await message.answer(text, parse_mode='html')




