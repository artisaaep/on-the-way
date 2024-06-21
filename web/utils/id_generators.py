from shared.base_models import Trip
from shared.database import get_db


def trip_generator():
    db = next(get_db())
    _id = db.query(Trip).order_by(Trip.id.desc()).first()
    return _id.id + 1 if _id else 1
