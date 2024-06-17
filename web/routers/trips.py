from fastapi import APIRouter, HTTPException
from typing import List
from ..data_models import Trip, NewTrip

router = APIRouter(
    prefix="/trips",
)


@router.get("/", response_model=List[Trip])
async def get_trips():
    pass


@router.post("/", response_model=int)
async def create_trip(new_trip: NewTrip):
    pass


@router.get("/{id}", response_model=Trip)
async def get_trip(_id: int):
    pass


@router.delete("/{id}", response_model=List[int])
async def delete_trip(_id: int, is_canceled: bool):
    pass


@router.put("/{id}/driver", response_model=None)
async def update_trip(_id: int, trip: Trip):
    pass


@router.put("/{id}/rider", response_model=None)
async def attach_rider(_id: int, trip: Trip):
    pass
