from pydantic import BaseModel


class GroupBase(BaseModel):
    id: int
    name: str


class GroupCreate(GroupBase):
    pass


class GroupInDBBase(GroupBase):
    class Config:
        orm_mode: True


class Group(GroupInDBBase):
    pass


class GroupInDB(GroupInDBBase):
    pass
