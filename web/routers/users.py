from pathlib import Path

from fastapi import APIRouter, HTTPException, Depends, Response, status
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


@router.put("/")
def update_user(new_user: User, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == new_user.id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User to update is not found")
    user_attrs = {
        attr: value for attr, value in vars(new_user).items() if not attr.startswith('_') and attr != 'metadata'
    }
    user_attrs['car_ids'] = None if new_user.car_ids is None else ' '.join(map(str, new_user.car_ids))
    for (key, value) in user_attrs.items():
        setattr(user, key, value)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
