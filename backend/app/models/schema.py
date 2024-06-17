from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime
from enum import Enum


class Group(BaseModel):
    groupUID: str
    name: str
    members: List[str]


class TransportMethod(str, Enum):
    flight = 'flight'
    train = 'train'
    car_rental = 'car_rental'


class ItemStatus(str, Enum):
    packed = 'packed'
    not_packed = 'not_packed'


class Member(BaseModel):
    memberUID: str
    nickName: str
    email: str
    password: str
    created_at: Optional[datetime]


class PaymentDetails(BaseModel):
    date: datetime
    by: str
    shared_by: List[str]
    amount: float


class Place(BaseModel):
    ticket: str
    time_of_appointment: datetime
    description: str
    payments: Optional[List[PaymentDetails]]


class Accommodation(BaseModel):
    address: str
    from_date: datetime
    to_date: datetime
    description: str
    paid_by: str


class RentalCarDetails(BaseModel):
    rented_by: str
    from_date: datetime
    to_date: datetime
    pickup_location: str
    return_location: str
    payment: PaymentDetails
    description: str


class Transport(BaseModel):
    method: TransportMethod
    ticket: str
    train_flight_number: str
    price: float
    time: datetime
    from_location: str
    to_location: str
    description: str
    paid_by: str
    rental_car: Optional[RentalCarDetails]


class TravelPlanner(BaseModel):
    planner_id: str
    date_from: datetime
    date_to: datetime
    location: str
    places_to_visit: List[Place]
    accommodations: List[Accommodation]
    transportation: List[Transport]
    members: List[str]


class GroupItem(BaseModel):
    item_id: str
    name: str
    claimed_by: Optional[str]
    payment: Optional[PaymentDetails]
    status: ItemStatus
    description: str


class PersonalItem(BaseModel):
    item_id: str
    name: str
    status: ItemStatus
    description: str


class MemberTransaction(BaseModel):
    member_id: str
    amount: float  # positive for credit, negative for debit


class Payment(BaseModel):
    payment_id: str
    group_id: str
    transactions: Dict[str, List[MemberTransaction]]
