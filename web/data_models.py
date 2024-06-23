from pydantic import BaseModel
from typing import List, Optional

from sqlalchemy.orm import Session

from shared.database import get_db
from shared.base_models import Trip as SQLTrip, Car as SQLCar
from web.utils.id_generators import trip_generator


class Car(BaseModel):
    id: Optional[int]
    owner_id: Optional[int]
    number: Optional[str]
    brand: str
    color: Optional[str]


class Driver(BaseModel):
    id: int
    name: str
    age: Optional[int]
    alias: str
    rides_amount: Optional[int]
    bio: Optional[str]
    car_ids: Optional[List[int]]


class Passenger(BaseModel):
    id: int
    name: str
    age: Optional[int]
    alias: str
    has_luggage: Optional[int]
    has_kids: Optional[int]
    has_pets: Optional[int]


class Trip(BaseModel):
    id: int
    driver: Driver
    passengers: List[Passenger]
    start_location: str
    end_location: str
    departure_time: str
    available_seats: Optional[int]
    has_child_seat: Optional[bool]
    car: Optional[Car]

    def to_orm(self) -> SQLTrip:
        passenger_ids = " ".join(str(p.id) for p in self.passengers)
        sqlalchemy_trip = Trip(
            id=self.id,
            driver_id=self.driver.id,
            passenger_ids=passenger_ids,
            start_location=self.start_location,
            end_location=self.end_location,
            departure_time=self.departure_time,
            seats_available=self.available_seats,
            has_child_seat=self.has_child_seat,
            car_id=self.car.id if self.car else None
        )
        return sqlalchemy_trip


class NewTrip(BaseModel):
    driver_id: int
    start_location: str
    end_location: str
    departure_time: str
    end_location: str
    available_seats: Optional[int]
    has_child_seat: Optional[bool]
    car_id: Optional[int]

    def to_full(self, db: Session = get_db()) -> Trip:
        return Trip(
            driver_id=self.driver_id,
            start_location=self.start_location,
            end_location=self.end_location,
            departure_time=self.departure_time,
            seats_available=self.available_seats,
            has_child_seat=self.has_child_seat,
            car_id=self.car_id,
            id=trip_generator(),
            passenger_ids=[],
            car=db.query(SQLCar).filter_by(id=self.car_id).one_or_none() if self.car else None
        )


class User(BaseModel):
    id: int
    name: Optional[str] = None
    age: Optional[int]
    bio: Optional[str] = None
    alias: str
    carIds: List[int]
