from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.record import Record
from app.schemas.record import RecordCreate
from app.core.security import get_current_user, require_role

router = APIRouter()


#  Create record (admin only)
@router.post("/")
def create_record(
    record: RecordCreate,
    db: Session = Depends(get_db),
    user = Depends(require_role(["admin"]))
):
    new_record = Record(
        title=record.title,
        amount=record.amount,
        category=record.category,
        user_id=user.id
    )

    db.add(new_record)
    db.commit()
    db.refresh(new_record)

    return new_record


#  Get all records (any logged user)
@router.get("/")
def get_records(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    return db.query(Record).all()