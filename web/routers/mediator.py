from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from fastapi import APIRouter, HTTPException, Depends, Query, Response, status
from sqlalchemy.orm import Session
from typing import List

from telegram.config_reader import config
from web.data_models import Trip, NewTrip, UserOptions
from shared.database import get_db
from shared.base_models import Trip as SQLTrip, User as SQLUser, TripPassenger, User

router = APIRouter(
    prefix="/api/mediator",
)

bot = Bot(token=config.bot_token.get_secret_value())


@router.post("/await_submission")
async def await_submission(

        rider_options: UserOptions,
        db: Session = Depends(get_db),
        rider_id: int = Query(..., alias="riderId"),
        driver_id: int = Query(..., alias="driverId"),
):
    rider: User = db.query(User).filter(User.id == rider_id).first()
    options_text = ""
    if rider_options.has_kids == 1:
        options_text += "C ребёнком."
    elif rider_options.has_kids > 1:
        options_text += f"C {int(rider_options.has_kids)} детьми."
    if rider_options.has_luggage:
        options_text += "C багажом."
    if rider_options.has_pets:
        options_text += "С животным."

    await bot.send_message(
        chat_id=driver_id,
        text=f"К вашей поездке хочет присоединиться *{rider.name}*. {options_text}",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="✅Принять", callback_data="hi")],
            [InlineKeyboardButton(text="❌Отклонить", callback_data="hello")],
            [InlineKeyboardButton(text=f"Профиль пользователя {rider.name}", url=f"tg://user?id={rider_id}",
                                  callback_data="bye")]
        ]),
        parse_mode="Markdown"
    )
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{_id}/rider")
async def attach_rider(
        _id: int,
        rider_options: UserOptions,
        rider_id: int = Query(..., alias="riderID"),
        db: Session = Depends(get_db)
):
    passengers, db_trip = __check_rider_properties(db, _id, rider_id)
    if str(rider_id) not in passengers:
        passengers.append(str(rider_id))
        db_trip.passenger_ids = ' '.join(passengers)
    else:
        raise HTTPException(status_code=400, detail="Bad request. Rider already attached to the ride")

    trip_rider_attrs = {
        attr: value for attr, value in vars(rider_options).items() if
        not attr.startswith('_') and attr != 'metadata'
    }
    trip_rider_attrs["user_id"] = rider_id
    trip_rider_attrs["trip_id"] = _id
    db.add(TripPassenger(**trip_rider_attrs))
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/{_id}/rider")
async def cansel_rider(
        _id: int,
        rider_id: int = Query(..., alias="riderID"),
        db: Session = Depends(get_db)
):
    passengers, db_trip = __check_rider_properties(db, _id, rider_id)
    if str(rider_id) in passengers:
        passengers.remove(str(rider_id))
        db_trip.passenger_ids = ' '.join(passengers)
    else:
        raise HTTPException(status_code=400, detail="Bad request. Rider is not attached to the ride")

    db.delete(
        db.query(TripPassenger).filter(TripPassenger.user_id == rider_id,
                                       TripPassenger.trip_id == _id).first())
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def __check_rider_properties(db: Session, _id: int, rider_id: int) -> (List[str], SQLTrip):
    db_trip = db.query(SQLTrip).filter(SQLTrip.id == _id).first()
    if db_trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    passenger = db.query(SQLUser).filter(SQLUser.id == rider_id).first()
    if passenger is None:
        raise HTTPException(status_code=404, detail="Rider have not authorized")
    if db_trip.driver_id == rider_id:
        raise HTTPException(status_code=400, detail="Bad request. Driver cannot be rider of his ride")
    if db_trip.passenger_ids:
        passengers = [*map(lambda s: s.strip(), db_trip.passenger_ids.split())]
    else:
        passengers = []
    return passengers, db_trip
