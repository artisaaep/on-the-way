from typing import Optional

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from shared.base_models import User, Base


class Database:
    def __init__(self):
        self.db = Depends(get_db())

    def exists(self, user_id: int) -> bool:
        return self.db.query(User).filter(User.id == user_id).first() is not None

    def create_profile(self, user_id: int, name: str = "", age: int = 0, sex: int = -1, photo: str = "", bio: str = "",
                       alias: str = "") -> None:
        user = User(id=user_id, name=name, age=age, sex=sex, photo=photo, bio=bio, alias=alias)
        self.db.add(user)
        self.db.commit()

    def update_profile(self, user_id: int, name: Optional[str] = None, age: Optional[int] = None,
                       sex: Optional[int] = None, photo: Optional[str] = None, bio: Optional[str] = None) -> None:
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ValueError("User not found")
        if name is not None:
            user.name = name
        if age is not None:
            user.age = age
        if sex is not None:
            user.sex = sex
        if photo is not None:
            user.photo = photo
        if bio is not None:
            user.bio = bio
        self.db.commit()

    def get_photo(self, user_id: int) -> str:
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ValueError("User not found")
        return user.photo


DATABASE_URL = "sqlite:///./db.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables
Base.metadata.create_all(bind=engine)


# Dependency to get DB session
def get_db() -> SessionLocal:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
