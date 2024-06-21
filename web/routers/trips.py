# trips.py
from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from ..data_models import Trip, NewTrip, Driver
from shared.database import get_db
from shared.base_models import Trip as TripModel, User
from ..utils.id_generators import trip_generator

router = APIRouter(
    prefix="/trips",
)


@router.get("/", response_model=List[Trip])
async def get_trips(db: Session = Depends(get_db)):
    trips = db.query(TripModel).all()
    return [
        Trip(
            id=trip.id,
            driver=Driver(
                id=trip.driver.id,
                name=trip.driver.name,
                age=trip.driver.age,
                alias=trip.driver.alias,
                rides_amount=trip.driver.rides_amount,
                bio=trip.driver.bio,
                car_ids=trip.driver.car_ids.split(',') if trip.driver.car_ids else []
            ),
            passengers=[],  # Assuming you handle passengers separately
            start_location=trip.start_location,
            end_location=trip.end_location,
            departure_time=trip.departure_time,
            available_seats=trip.available_seats,
            has_child_seat=trip.has_child_seat,
            car=trip.car,
        ) for trip in trips
    ]


@router.post("/", response_model=int)
async def create_trip(new_trip: NewTrip, db: Session = Depends(get_db)):
    trip_id = trip_generator()
    driver = db.query(User).get(new_trip.driver_id)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")

    driver_pydantic = Driver(
        id=driver.id,
        name=driver.name,
        age=driver.age,
        alias=driver.alias,
        rides_amount=driver.rides_amount,
        bio=driver.bio,
        car_ids=driver.car_ids.split(',') if driver.car_ids else []
    )

    trip = TripModel(
        id=trip_id,
        driver=driver_pydantic,
        start_location=new_trip.start_location,
        end_location=new_trip.end_location,
        departure_time=new_trip.departure_time,
        available_seats=new_trip.available_seats if new_trip.available_seats is not None else 4,
        has_child_seat=new_trip.has_child_seat if new_trip.has_child_seat else False,
        car=new_trip.car if new_trip.car is not None else ""
    )

    db.add(trip)
    db.commit()
    db.refresh(trip)
    return trip.id


@router.get("/{id}", response_model=Trip)
async def get_trip(_id: int, db: Session = Depends(get_db)):
    trip = db.query(TripModel).filter(TripModel.id == _id).first()
    if trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip


@router.delete("/{id}", response_model=List[int])
async def delete_trip(_id: int, db: Session = Depends(get_db), is_canceled: bool = True):
    trip = db.query(TripModel).filter(TripModel.id == _id).first()
    if trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    db.delete(trip)
    db.commit()
    return [trip.id]


@router.put("/{id}/driver", response_model=None)
async def update_trip(_id: int, trip: Trip, driver_id: int = 0, db: Session = Depends(get_db)):
    db_trip = db.query(TripModel).filter(TripModel.id == _id).first()
    if db_trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    for key, value in trip.dict().items():
        setattr(db_trip, key, value)
    db.commit()
    return


@router.put("/{id}/rider", response_model=None)
async def attach_rider(
        _id: int,
        rider_id: int = Query(..., alias="riderID"),
        db: Session = Depends(get_db)
):
    db_trip = db.query(TripModel).filter(TripModel.id == _id).first()
    if db_trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")

    # Assuming passengers are stored as a comma-separated string of IDs
    if db_trip.passengers:
        passengers = map(lambda s: s.trim, db_trip.passengers.split(','))
    else:
        passengers = []

    if str(rider_id) not in passengers:
        passengers.append(str(rider_id))
        db_trip.passengers = ','.join(passengers)
        db.commit()

    return
