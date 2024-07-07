from fastapi import APIRouter, HTTPException, Depends, Query, Response, status
from sqlalchemy.orm import Session
from typing import List
from web.data_models import Trip, NewTrip, UserOptions
from shared.database import get_db
from shared.base_models import Trip as SQLTrip, User as SQLUser, TripPassenger

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
        attr: value for attr, value in vars(rider_options).items() if not attr.startswith('_') and attr != 'metadata'
    }
    trip_rider_attrs["user_id"] = rider_id
    trip_rider_attrs["trip_id"] = _id
    db.add(TripPassenger(**trip_rider_attrs))
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/{_id}/rider")
async def attach_rider(
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
                                       TripPassenger.trip_id.like == _id).first())
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
