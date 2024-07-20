from fastapi import APIRouter, HTTPException, Depends, Response, status
from sqlalchemy.orm import Session
from web.data_models import NewCar, Car
from web.utils.id_generators import generator
from shared.database import get_db
from shared.base_models import Car as SQLCar, User as SQLUser

router = APIRouter(
    prefix="/api/cars",
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
    id_ = generator(SQLCar)
    car = SQLCar(
        id=id_,
        owner_id=new.owner_id,
        number=new.number,
        brand=new.brand,
        color=new.color,
    )
    owner = db.query(SQLUser).filter(SQLUser.id == new.owner_id).first()
    owner.car_ids = (owner.car_ids + f" {id_}") if owner.car_ids else f"{id_}"
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
    if car.owner_id is not None:
        user: SQLUser = db.query(SQLUser).filter(SQLUser.id == car.owner_id).first()
        user.car_ids = ' '.join(_id for _id in user.car_ids.split() if _id != int(car.id))
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
