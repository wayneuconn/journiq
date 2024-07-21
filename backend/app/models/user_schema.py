from enum import Enum

from pydantic import BaseModel
from datetime import datetime


class Role(str, Enum):
    admin = 'admin'
    member = 'member'


class GroupBase(BaseModel):
    groupUID: str
    name: str


class Member(BaseModel):
    memberUID: str
    nickName: str
    email: str
    password: str
    created_at: datetime
    role: Role = Role.member
    groups: list[GroupBase] = []

    class Config:
        orm_mode = True
