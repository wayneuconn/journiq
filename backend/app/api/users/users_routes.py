from app.models.users.user import UserCreate, UserUpdate, UserBase
from app.api.users import user as user_api
from fastapi import APIRouter, HTTPException

public_router = APIRouter()


@public_router.post("/users/", response_model=UserBase)
async def create_user(user: UserCreate):
    user = await user_api.create_user(user)
    return {**user.dict()}


@public_router.get("/users/{user_id}", response_model=UserBase)
async def read_user(user_id: int):
    db_user = await user_api.get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@public_router.put("/users/{user_id}", response_model=UserUpdate)
async def update_user(user_id: int, user: UserUpdate):
    return await user_api.update_user(user_id, user)


@public_router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    return await user_api.delete_user(user_id)
