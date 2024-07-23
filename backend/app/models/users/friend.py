from pydantic import BaseModel


class FriendBase(BaseModel):
    userId: int
    friendId: int


class FriendCreate(FriendBase):
    pass


class FriendInDBBase(FriendBase):
    id: int

    class Config:
        orm_mode: True


class Friend(FriendInDBBase):
    pass


class FriendInDB(FriendInDBBase):
    pass
