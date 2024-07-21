from shared.database import get_db


def generator(cls_orm):
    db = next(get_db())
    _id = db.query(cls_orm).order_by(cls_orm.id.desc()).first()
    return _id.id + 1 if _id else 1

