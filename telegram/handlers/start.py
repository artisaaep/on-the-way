from aiogram import Router
from aiogram.filters import CommandStart
from aiogram import types
from shared.database_class import Database
from ..config_reader import base_webapp_url
from ..form import Form
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from telegram.bot_init import bot
from aiogram.fsm.state import State, StatesGroup

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
        await state.set_state(Form.number)
        await message.answer(text, reply_markup=markup, parse_mode='html')
    else:
        builder = InlineKeyboardBuilder()
        builder.row(InlineKeyboardButton(text="Создать поездку",
                                         web_app=WebAppInfo(url=base_webapp_url + "/app/createTrip.html")),
                    InlineKeyboardButton(text="Найти поездку",
                                         web_app=WebAppInfo(url=base_webapp_url + "/app/availabletrips.html")))
        builder.row(InlineKeyboardButton(text="Мой профиль",
                                         web_app=WebAppInfo(url=base_webapp_url + "/app/profile.html")))
        builder.row(InlineKeyboardButton(text="Оставить обратную связь", callback_data='feedback'))
        text = "Привет!\n\nЭто сервис по поиску попутчиков <b>on the way</b>. \
Здесь вы можете найти с кем добраться до пункта назначения или создать поездку как водитель и найти пассажиров. \U0001F699 "
        await message.answer(text, parse_mode='html', reply_markup=builder.as_markup())

class Feedback(StatesGroup):
    feedback = State()

@router.callback_query(lambda c: c.data == 'feedback')
async def process_feedback_button(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback_query.from_user.id, "Пожалуйста, оставьте ваше сообщение")
    await state.set_state(Feedback.feedback)

@router.message(Feedback.feedback)
async def getFeedback(message: types.Message, state: FSMContext):
    feedback = message.text
    await message.answer("Спасибо за ваше обращение! Оно будет рассмотрено в ближайшее время.")
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Создать поездку",
                                        web_app=WebAppInfo(url=base_webapp_url + "/app/createTrip.html")),
                InlineKeyboardButton(text="Найти поездку",
                                        web_app=WebAppInfo(url=base_webapp_url + "/app/availabletrips.html")))
    builder.row(InlineKeyboardButton(text="Мой профиль",
                                        web_app=WebAppInfo(url=base_webapp_url + "/app/profile.html")))
    builder.row(InlineKeyboardButton(text="Оставить обратную связь", callback_data='feedback'))
    text = "Привет!\n\nЭто сервис по поиску попутчиков <b>on the way</b>. \
Здесь вы можете найти с кем добраться до пункта назначения или создать поездку как водитель и найти пассажиров. \U0001F699 "
    await message.answer(text, parse_mode='html', reply_markup=builder.as_markup())
