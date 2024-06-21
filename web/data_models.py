from pydantic import BaseModel
from typing import List, Optional


class NewTrip(BaseModel):
    driver_id: int
    start_location: str
    end_location: str
    departure_time: str
    end_location: str
    available_seats: Optional[int]
    has_child_seat: Optional[bool]
    car: Optional[str]


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
    car: Optional[str]


class User(BaseModel):
    id: int
    name: Optional[str] = None
    age: Optional[int]
    bio: Optional[str] = None
    alias: str
    carIds: List[int]
