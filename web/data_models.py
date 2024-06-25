from pydantic import BaseModel
from typing import List, Optional, Any

from sqlalchemy.orm import Session

from shared.database import get_db
from shared.base_models import Trip as SQLTrip, Car as SQLCar, TripPassenger
from web.utils.id_generators import generator


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

    @staticmethod
    def from_orm(orm: SQLTrip, session: Session = get_db()):
        sql_driver = orm.driver
        body_driver = Driver(
            id=sql_driver.id,
            name=sql_driver.name,
            age=sql_driver.age,
            alias=sql_driver.alias,
            rides_amount=sql_driver.rides_amount,
            bio=None,
            car_ids=list(map(int, sql_driver.car_ids.split())),
        )
        passenger_ids = map(int, orm.passenger_ids.split()) if orm.passenger_ids else []
        passengers = []
        for pid in passenger_ids:
            user = session.query(User).get(int(pid))
            trip_passenger = session.query(TripPassenger).filter_by(user_id=user.id, trip_id=orm.id).first()
            if user:
                passengers.append(
                    Passenger(
                        id=user.id,
                        name=user.name,
                        age=user.age,
                        alias=user.alias,
                        has_luggage=trip_passenger.has_luggage if trip_passenger else 0,
                        has_kids=trip_passenger.has_kids if trip_passenger else 0,
                        has_pets=trip_passenger.has_pets if trip_passenger else 0
                    )
                )

        trip_model = Trip(
            id=orm.id,
            driver=body_driver,
            passengers=passengers,
            start_location=orm.start_location,
            end_location=orm.end_location,
            departure_time=orm.departure_time,
            available_seats=orm.seats_available,
            has_child_seat=orm.has_child_seat,
            car=session.query(Car).filter_by(id=orm.car_id).first(),
        )

        return trip_model


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
            id=generator(SQLTrip),
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
