from enum import Enum

from pydantic import BaseModel

from app.models.payment_schema import PaymentDetails


class ItemStatus(str, Enum):
    packed = "packed"
    not_packed = "not_packed"


class GroupItem(BaseModel):
    item_id: str
    name: str
    claimed_by: str | None
    payment: PaymentDetails | None
    status: ItemStatus
    description: str


class PersonalItem(BaseModel):
    item_id: str
    name: str
    status: ItemStatus
    description: str
