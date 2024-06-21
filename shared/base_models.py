from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=True)
    age = Column(Integer, nullable=True)
    sex = Column(Integer, nullable=True)
    photo = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    alias = Column(String, unique=True, index=True)


class Trip(Base):
    __tablename__ = 'trips'

    id = Column(Integer, primary_key=True, index=True)
    driver_id = Column(Integer, ForeignKey('users.id'))
    driver = relationship("User")
    passengers = Column(String, nullable=True)  # Assuming passengers are stored as comma-separated string
    start_location = Column(String, index=True)
    end_location = Column(String, index=True)
    departure_time = Column(String, index=True)
    available_seats = Column(Integer, nullable=True)
    has_child_seat = Column(Boolean, nullable=True)
    car = Column(String, nullable=True)
