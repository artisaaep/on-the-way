from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ..data_models import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/{user_id}", response_model=User)
def read_user(user_id: int):
    pass


@router.get("/{user_id}/photo", response_model=str)
def read_user_photo(user_id: int):
    pass
