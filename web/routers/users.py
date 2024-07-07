from pathlib import Path

from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from web.data_models import User
from shared.database import get_db
from shared.base_models import User as UserModel

router = APIRouter(
    prefix="/api/users",
    tags=["users"],
)


@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return User.from_orm(user)


@router.get("/{user_id}/photo")
def read_user_photo(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    image_path = Path(__file__).parent.parent.parent / "shared" / "photos" / (str(user_id) + '.jpg')
    return FileResponse(image_path)

