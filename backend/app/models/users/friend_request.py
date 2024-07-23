from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class FriendRequestStatus(str, Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"


class FriendRequestBase(BaseModel):
    senderId: int
    receiverId: int
    status: FriendRequestStatus = FriendRequestStatus.PENDING


class FriendRequestCreate(FriendRequestBase):
    pass


class FriendRequestUpdate(BaseModel):
    status: FriendRequestStatus | None = None


class FriendRequestInDBBase(FriendRequestBase):
    id: int
    createdAt: datetime

    class Config:
        orm_mode: True


class FriendRequest(FriendRequestInDBBase):
    pass


class FriendRequestInDB(FriendRequestInDBBase):
    pass
