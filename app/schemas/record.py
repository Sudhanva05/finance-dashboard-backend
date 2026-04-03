from pydantic import BaseModel

class RecordCreate(BaseModel):
    title: str
    amount: float
    category: str