from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.record import Record
from app.schemas.record import RecordCreate
from app.core.security import get_current_user, require_role
from typing import Optional

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
    category: Optional[str] = None,
    min_amount: Optional[float] = None,
    max_amount: Optional[float] = None,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    query = db.query(Record)

    if category:
        query = query.filter(Record.category == category)

    if min_amount:
        query = query.filter(Record.amount >= min_amount)

    if max_amount:
        query = query.filter(Record.amount <= max_amount)

    return query.all()

@router.get("/summary")
def get_summary(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    records = db.query(Record).all()

    total_income = sum(r.amount for r in records if r.category.lower() == "income")
    total_expense = sum(r.amount for r in records if r.category.lower() == "expense")

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": total_income - total_expense
    }