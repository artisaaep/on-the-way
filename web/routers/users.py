# users.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..data_models import User
from shared.database import get_db
from shared.base_models import User as UserModel

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/{user_id}/photo", response_model=str)
def read_user_photo(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.photo
