from pydantic import BaseModel
from typing import List, Optional, Any

from pydantic.main import Model
from sqlalchemy.orm import Session

from shared.database import get_db
from shared.base_models import Trip as SQLTrip, Car as SQLCar, TripPassenger, User as SQLUser
from web.utils.id_generators import generator


class NewCar(BaseModel):
    owner_id: Optional[int]
    number: Optional[str]
    brand: str
    color: Optional[str]


class Car(NewCar):
    model_config = {"from_attributes": True}
    id: int


class User(BaseModel):
    model_config = {"from_attributes": True}

    id: int
    name: Optional[str] = None
    age: Optional[int]
    alias: str
    sex: int
    car_ids: List[int]
    rides_amount: Optional[int]

    @classmethod
    def from_orm(cls: type[BaseModel], obj: SQLUser) -> Model:
        return cls(
            id=obj.id,
            name=obj.name,
            age=obj.age,
            alias=obj.alias,
            sex=obj.sex,
            car_ids=map(int, obj.car_ids.split()) if obj.car_ids else [],
            rides_amount=obj.rides_amount,
        )


class Passenger(User):
    has_luggage: Optional[int]
    has_kids: Optional[int]
    has_pets: Optional[int]


class BaseTrip(BaseModel):
    start_location: str
    end_location: str
    departure_time: str
    end_location: str
    price: int
    available_seats: Optional[int]
    has_child_seat: Optional[bool]
    departure_date: Optional[str]
    clarify_from: Optional[str]
    clarify_to: Optional[str]

    model_config = {"from_attributes": True}


class Trip(BaseTrip):
    id: int
    driver: User
    passengers: List[Passenger]
    car: Optional[Car]

    def to_orm(self) -> SQLTrip:
        passenger_ids = " ".join(str(p.id) for p in self.passengers)
        sqlalchemy_trip = SQLTrip(
            id=self.id,
            driver_id=self.driver.id,
            passenger_ids=passenger_ids if passenger_ids else "",
            start_location=self.start_location,
            end_location=self.end_location,
            departure_time=self.departure_time,
            seats_available=self.available_seats,
            has_child_seat=self.has_child_seat,
            price=self.price,
            car_id=self.car.id if self.car else 0,
            departure_date=self.departure_date,
            clarify_from=self.clarify_from,
            clarify_to=self.clarify_to,
        )
        return sqlalchemy_trip

    @classmethod
    def from_orm(cls, orm: SQLTrip):
        session = next(get_db())
        sql_driver = orm.driver
        body_driver = User(
            id=sql_driver.id,
            name=sql_driver.name,
            age=sql_driver.age,
            alias=sql_driver.alias,
            rides_amount=sql_driver.rides_amount,
            bio=None,
            car_ids=list(map(int, sql_driver.car_ids.split())) if sql_driver.car_ids else [],
        )
        passenger_ids = map(int, orm.passenger_ids.split()) if orm.passenger_ids else []
        passengers = []
        for pid in passenger_ids:
            user = session.query(SQLUser).get(int(pid))
            trip_passenger = session.query(TripPassenger).filter_by(user_id=user.id, trip_id=orm.id).first()
            if user:
                passengers.append(
                    Passenger(
                        id=user.id,
                        name=user.name,
                        age=user.age,
                        alias=user.alias,
                        rides_amount=user.rides_amount,
                        car_ids=list(map(int, user.car_ids.split())) if user.car_ids else [],
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
            price=orm.price,
            car=session.query(SQLCar).filter(SQLCar.id == orm.car_id).first(),
            departure_date=orm.departure_date,
            clarify_from=orm.clarify_from,
            clarify_to=orm.clarify_to,
        )

        return trip_model


class NewTrip(BaseTrip):
    car_id: Optional[int]
    driver_id: int

    def to_full(self, db: Session = next(get_db())):  # -> Trip
        return Trip(
            passengers=[],
            id=generator(SQLTrip),
            car=db.query(SQLCar).filter(SQLCar.id == self.car_id).first() if self.car_id else 0,
            driver=User.from_orm(db.query(SQLUser).filter(SQLUser.id == self.driver_id).first()),
            start_location=self.start_location,
            end_location=self.end_location,
            departure_time=self.departure_time,
            available_seats=self.available_seats,
            has_child_seat=self.has_child_seat,
            price=self.price,
            departure_date=self.departure_date,
            clarify_from=self.clarify_from,
            clarify_to=self.clarify_to,
        )


class UserOptions(BaseModel):
    has_luggage: bool
    has_kids: bool
    has_pets: bool
