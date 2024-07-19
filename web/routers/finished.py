from fastapi import APIRouter, HTTPException, Depends, Query, Response, status
from sqlalchemy.orm import Session
from typing import List
from web.data_models import Trip
from shared.database import get_db
from shared.base_models import FinishedTrip as SQLTrip, User as SQLUser

router = APIRouter(
    prefix="/api/finished",
)


@router.get("/{user_id}", response_model=List[Trip])
async def get_trips(user_id: int, db: Session = Depends(get_db)):
    trips = db.query(SQLTrip).filter(SQLTrip.driver_id == user_id).all()
    return [Trip.from_orm(trip) for trip in trips if trip is not None]
