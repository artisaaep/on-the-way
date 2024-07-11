from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship, Session

from shared.database import get_db, Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=True)
    age = Column(Integer, nullable=True)
    sex = Column(Integer, nullable=True)
    alias = Column(String, unique=True, index=True)
    rides_amount = Column(Integer, default=0)
    car_ids = Column(String, nullable=True)
    number = Column(String, index=True, nullable=True)


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


class Trip(Base):
    __tablename__ = 'trips'

    id = Column(Integer, primary_key=True, index=True)
    driver_id = Column(Integer, ForeignKey('users.id'))
    driver = relationship("User", back_populates="driven_trips")
    passenger_ids = Column(String, nullable=True)  # space-sliced integers
    start_location = Column(String, index=True)
    end_location = Column(String, index=True)
    price = Column(Integer, nullable=True)
    departure_time = Column(String, index=True)
    seats_available = Column(Integer, nullable=True)
    has_child_seat = Column(Boolean, nullable=True)
    car_id = Column(Integer, ForeignKey('cars.id'), nullable=True)
    car = relationship("Car")
    departure_date = Column(String, nullable=True)
    clarify_from = Column(String, nullable=True)
    clarify_to = Column(String, nullable=True)


User.cars = relationship("Car", order_by=Car.id, back_populates="owner")
User.trips = relationship("TripPassenger", order_by=TripPassenger.trip_id, back_populates="user")
User.driven_trips = relationship("Trip", order_by=Trip.id, back_populates="driver")
