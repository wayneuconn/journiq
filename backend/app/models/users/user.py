from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum
from app.models.users.friend import Friend
from app.models.users.friend_request import FriendRequest
from app.models.users.group import Group


class Role(str, Enum):
    admin = "ADMIN"
    member = "MEMBER"


class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: Role = Role.member


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None


class UserInDBBase(UserBase):
    id: int
    createdAt: datetime
    updatedAt: datetime

    class Config:
        orm_mode: True


class User(UserInDBBase):
    sentRequests: list[FriendRequest] = []
    receivedRequests: list[FriendRequest] = []
    friends: list[Friend] = []
    groups: list[Group] = []


class UserInDB(UserInDBBase):
    password: str
