from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session

from shared.database import get_db
from web.data_models import Driver, Trip as PydanticTrip, Passenger

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=True)
    age = Column(Integer, nullable=True)
    sex = Column(Integer, nullable=True)
    alias = Column(String, unique=True, index=True)
    rides_amount = Column(Integer)
    car_ids = Column(String, nullable=True)


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    number = Column(String, nullable=True)
    brand = Column(String, nullable=True)
    color = Column(String, nullable=True)
    owner = relationship("User", back_populates="cars")


class TripPassenger(Base):
    __tablename__ = 'trip_passenger'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    trip_id = Column(Integer, ForeignKey('trips.id'), primary_key=True)
    has_luggage = Column(Boolean, nullable=True)
    has_kids = Column(Boolean, nullable=True)
    has_pets = Column(Boolean, nullable=True)
    user = relationship("User", back_populates="trips")
    trip = relationship("Trip", back_populates="passengers")


class Trip(Base):
    __tablename__ = 'trips'

    id = Column(Integer, primary_key=True, index=True)
    driver_id = Column(Integer, ForeignKey('users.id'))
    driver = relationship("User", back_populates="driven_trips")
    passenger_ids = Column(String, nullable=True)  # space-sliced integers
    start_location = Column(String, index=True)
    end_location = Column(String, index=True)
    departure_time = Column(String, index=True)
    seats_available = Column(Integer, nullable=True)
    has_child_seat = Column(Boolean, nullable=True)
    car_id = Column(Integer, ForeignKey('cars.id'), nullable=True)
    car = relationship("Car")

    def to_pydantic(self, session: Session = get_db()) -> PydanticTrip:
        sql_driver = self.driver
        body_driver = Driver(
            id=sql_driver.id,
            name=sql_driver.name,
            age=sql_driver.age,
            alias=sql_driver.alias,
            rides_amount=sql_driver.rides_amount,
            bio=None,
            car_ids=list(map(int, sql_driver.car_ids.split())),
        )
        passenger_ids = map(int, self.passenger_ids.split()) if self.passenger_ids else []
        passengers = []
        for pid in passenger_ids:
            user = session.query(User).get(int(pid))
            trip_passenger = session.query(TripPassenger).filter_by(user_id=user.id, trip_id=self.id).first()
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

        trip_model = PydanticTrip(
            id=self.id,
            driver=body_driver,
            passengers=passengers,
            start_location=self.start_location,
            end_location=self.end_location,
            departure_time=self.departure_time,
            available_seats=self.seats_available,
            has_child_seat=self.has_child_seat,
            car=session.query(Car).filter_by(id=self.car_id).first(),
        )

        return trip_model


User.cars = relationship("Car", order_by=Car.id, back_populates="owner")
User.trips = relationship("TripPassenger", order_by=TripPassenger.trip_id, back_populates="user")
User.driven_trips = relationship("Trip", order_by=Trip.id, back_populates="driver")
