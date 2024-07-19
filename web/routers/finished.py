from fastapi import APIRouter, HTTPException, Depends, Query, Response, status
from sqlalchemy.orm import Session
from typing import List
from web.data_models import Trip
from shared.database import get_db
from shared.base_models import FinishedTrip as SQLTrip, User as SQLUser, PassengersHistory, FinishedTrip

router = APIRouter(
    prefix="/api/finished",
)


@router.get("/driver/{user_id}", response_model=List[Trip])
async def get_trips(user_id: int, db: Session = Depends(get_db)):
    trips = db.query(FinishedTrip).filter(FinishedTrip.driver_id == user_id).all()
    return [Trip.from_orm(trip) for trip in trips if trip is not None]


@router.get("/rider/{user_id}", response_model=List[Trip])
async def get_trips(user_id: int, db: Session = Depends(get_db)):
    applications = db.query(PassengersHistory).filter(PassengersHistory.user_id == user_id).all()
    trips = []
    for application in applications:
        trips.append(db.query(FinishedTrip).filter(FinishedTrip.id == application.trip_id).first())
    return [Trip.from_orm(trip) for trip in trips if trip is not None]
