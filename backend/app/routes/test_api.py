from fastapi import HTTPException, Request, APIRouter

from prisma.models import Member
from app.models.user_schema import Member as MemberSchema

public_router = APIRouter()


@public_router.post("/test_create_member", response_model=MemberSchema)
async def test_create_member(request: MemberSchema):
    data = request.json()
    try:
        new_member = await Member.create(data=data)
        return new_member
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
