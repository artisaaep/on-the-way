from fastapi import APIRouter, HTTPException, Depends, Response, status
from sqlalchemy.orm import Session
from ..data_models import NewCar, Car
from shared.database import get_db
from shared.base_models import Car as SQLCar
from ..utils.id_generators import generator

router = APIRouter(
    prefix="/cars",
)


@router.get("/{_id}", response_model=Car)
async def get_car(_id: int, db: Session = Depends(get_db)):
    car = db.query(SQLCar).filter(SQLCar.id == _id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return Car.from_orm(car)


@router.post("/", response_model=int)
async def create_car(new: NewCar,
                     db: Session = Depends(get_db)):
    car = SQLCar(
        id=generator(SQLCar),
        owner_id=new.owner_id,
        number=new.number,
        brand=new.brand,
        color=new.color,
    )
    db.add(car)
    db.commit()
    db.refresh(car)
    return car.id


@router.delete("/{_id}")
async def delete_car(_id: int, db: Session = Depends(get_db)):
    car = db.query(SQLCar).filter(SQLCar.id == _id).first()
    if car is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    db.delete(car)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
