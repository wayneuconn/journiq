from datetime import datetime
from enum import Enum

from pydantic import BaseModel

from app.models.payment_schema import PaymentDetails


class RentalCarDetails(BaseModel):
    rented_by: str
    from_date: datetime
    to_date: datetime
    pickup_location: str
    return_location: str
    payment: PaymentDetails
    description: str


class TransportMethod(str, Enum):
    flight = "flight"
    train = "train"
    car_rental = "car_rental"


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
    rental_car: RentalCarDetails | None


class Accommodation(BaseModel):
    address: str
    from_date: datetime
    to_date: datetime
    description: str
    paid_by: str


class Place(BaseModel):
    ticket: str
    time_of_appointment: datetime
    description: str
    payments: list[PaymentDetails] = []


class Destination(BaseModel):
    destination_id: str
    date_from: datetime
    date_to: datetime
    location: str
    places_to_visit: list[Place]
    accommodations: list[Accommodation]
    transportation: list[Transport]
    members: list[str]
