from datetime import datetime

from pydantic import BaseModel

from app.models.user_schema import Member


class MemberTransaction(BaseModel):
    member_id: str
    amount: float  # positive for credit, negative for debit


class Payment(BaseModel):
    payment_id: str
    group_id: str
    transactions: dict[str, list[MemberTransaction]]


class PaymentDetails(BaseModel):
    date: datetime
    by: str
    shared_by: list[Member]
    amount: float
