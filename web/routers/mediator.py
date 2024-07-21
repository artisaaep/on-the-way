from aiogram import Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from fastapi import APIRouter, HTTPException, Depends, Query, Response, status
from sqlalchemy.orm import Session

from shared.id_generators import generator
from telegram.config_reader import config
from web.data_models import Trip, NewTrip, UserOptions
from shared.database import get_db
from shared.base_models import Trip as SQLTrip, User as SQLUser, TripPassenger, User, SubmissionQueue

router = APIRouter(
    prefix="/api/mediator",
)

bot = Bot(token=config.bot_token.get_secret_value())


@router.post("/await_submission")
async def await_submission(
        rider_options: UserOptions,
        db: Session = Depends(get_db),
        rider_id: int = Query(..., alias="riderId"),
        trip_id: int = Query(..., alias="tripId"),
):
    # TODO: check if users are exists
    rider: User = db.query(User).filter(User.id == rider_id).first()
    trip: SQLTrip = db.query(SQLTrip).filter(SQLTrip.id == trip_id).first()
    driver_id = trip.driver_id
    options_text = ""
    if rider_options.has_kids == 1:
        options_text += "C ребёнком."
    elif rider_options.has_kids > 1:
        options_text += f"C {int(rider_options.has_kids)} детьми."
    if rider_options.has_luggage:
        options_text += "C багажом."
    if rider_options.has_pets:
        options_text += "С животным."

    node_id = generator(SubmissionQueue)
    callback_data = f'approve %s {node_id}'
    msg = await bot.send_message(
        chat_id=driver_id,
        text=f"К вашей поездке хочет присоединиться *{rider.name}*. {options_text}",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="✅Принять", callback_data=callback_data % '1')],
            [InlineKeyboardButton(text="❌Отклонить", callback_data=callback_data % '0')],
            [InlineKeyboardButton(text=f"Профиль пользователя {rider.name}", url=f"tg://user?id={rider_id}",
                                  callback_data="bye")]
        ]),
        parse_mode="Markdown"
    )
    db.add(
        SubmissionQueue(
            user_id=rider_id,
            trip_id=trip_id,
            submission_message_id=msg.message_id,
            id=node_id,
            has_kids=rider_options.has_kids,
            has_luggage=rider_options.has_luggage,
            has_pets=rider_options.has_pets,
        )
    )
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/await_submission")
async def reject_submission(
        db: Session = Depends(get_db),
        rider_id: int = Query(..., alias="riderId"),
        trip_id: int = Query(..., alias="tripId")):
    submission = db.query(SubmissionQueue).filter(SubmissionQueue.trip_id == trip_id,
                                                  SubmissionQueue.user_id == rider_id).first()
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if submission is None:
        print("Submission approved and cannot be rejected")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    await bot.delete_message(message_id=submission.submission_message_id, chat_id=trip.driver_id)
    db.delete(submission)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
