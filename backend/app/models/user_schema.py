import uuid
from dataclasses import Field
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
    memberUID: str | None = uuid.uuid4()
    nickName: str
    email: str
    password: str
    created_at: datetime | None = datetime.now()
    role: Role = Role.member
    groups: list[GroupBase] = []

    class Config:
        orm_mode = True
