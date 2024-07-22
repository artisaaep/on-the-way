from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from fastapi import APIRouter, HTTPException, Depends, Query, Response, status
from sqlalchemy.orm import Session
from typing import List

from telegram.config_reader import config
from web.data_models import Trip, NewTrip, UserOptions
from shared.database import get_db
from shared.base_models import Trip as SQLTrip, User as SQLUser, TripPassenger, SubmissionQueue

router = APIRouter(
    prefix="/api/trips",
)


@router.get("/", response_model=List[Trip])
async def get_trips(db: Session = Depends(get_db)):
    trips = db.query(SQLTrip).all()
    return [Trip.from_orm(trip) for trip in trips if trip is not None]


@router.post("/", response_model=int)
async def create_trip(new_trip: NewTrip, db: Session = Depends(get_db)):
    driver = db.query(SQLUser).get(new_trip.driver_id)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")

    sql_trip = new_trip.to_full().to_orm()

    db.add(sql_trip)
    async with Bot(token=config.bot_token.get_secret_value()) as bot:
        await bot.send_message(
            chat_id=sql_trip.driver_id,
            text=f"""Ваша поездка *{sql_trip.start_location} - ${sql_trip.end_location}* успешно создана! 🚙
\nНажмите на кнопку ниже, чтобы посмотреть подробную информацию о поездке или отредактировать ее ☺️""",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(
                    text="Подробнее",
                    web_app=WebAppInfo(
                        url=f"{config.base_webapp_url.get_secret_value()}/app/editTrip.html?${sql_trip.id}"
                    ))],
            ]),
            parse_mode="Markdown"
        )
    db.commit()
    db.refresh(sql_trip)
    return sql_trip.id


@router.get("/{_id}", response_model=Trip)
async def get_trip(_id: int, db: Session = Depends(get_db)):
    trip: SQLTrip = db.query(SQLTrip).filter(SQLTrip.id == _id).first()
    if trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    return Trip.from_orm(trip)


@router.delete("/{_id}", response_model=List[int])
async def delete_trip(_id: int, db: Session = Depends(get_db), is_canceled: bool = True):
    # todo: check for cancellation and raise telegram feedback process
    trip = db.query(SQLTrip).filter(SQLTrip.id == _id).first()
    if trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    db.delete(trip)
    db.commit()
    return [trip.id]


@router.put("/{_id}/driver")
async def update_trip(_id: int,
                      trip: Trip,
                      driver_id: int = Query(..., alias="driverID"),
                      db: Session = Depends(get_db)):
    db_trip = db.query(SQLTrip).filter(SQLTrip.id == _id).first()
    if db_trip.driver_id != driver_id or driver_id != trip.driver.id:
        raise HTTPException(status_code=403, detail="No access to change anther's trips")
    input_trip = trip.to_orm()
    if db_trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    trip_attrs = {
        attr: value for attr, value in vars(input_trip).items() if not attr.startswith('_') and attr != 'metadata'
    }
    for (key, value) in trip_attrs.items():
        setattr(db_trip, key, value)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/awaited/{user_id}", response_model=List[int])
async def join_trips_and_awaiters(user_id: int, db: Session = Depends(get_db)):
    return [awaiter.trip_id for awaiter in db.query(SubmissionQueue).filter(SubmissionQueue.user_id == user_id).all()]


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
    db_trip.seats_available += 1
    db.refresh(db_trip)
    db.commit()
    async with Bot(token=config.bot_token.get_secret_value()) as bot:
        await bot.send_message(chat_id=db_trip.driver_id,
                               text=f"Пользователь отказался от поездки с вами."
                                    + f"\nСвободных мест осталось: {db_trip.seats_available}"
                                    + f"\n{db_trip.departure_date}, {db_trip.departure_time}",
                               reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                   [InlineKeyboardButton(text=f"Профиль пользователя",
                                                         url=f"tg://user?id={rider_id}")]
                               ])
                               )
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# TODO: transfer it to mediator/awaitSubmission
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
