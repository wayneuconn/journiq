from prisma import Prisma
from app.models.users.user import UserCreate, UserUpdate
from prisma.models import User


async def create_user(user: UserCreate):
    return await User.prisma().create(data=user.dict())


async def get_user(user_id: int):
    return await User.prisma().find_unique(where={"id": user_id})


async def update_user(user_id: int, user: UserUpdate):
    return await User.prisma().update(where={"id": user_id}, data=user.dict(exclude_unset=True))


async def delete_user(user_id: int):
    return await User.prisma().delete(where={"id": user_id})
