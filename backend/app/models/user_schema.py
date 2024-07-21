from pydantic import BaseModel
from datetime import datetime


class Member(BaseModel):
    memberUID: str
    nickName: str
    email: str
    password: str
    created_at: datetime | None


class Group(BaseModel):
    groupUID: str
    name: str
    members: list[Member]

