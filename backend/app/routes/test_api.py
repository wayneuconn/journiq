from fastapi import HTTPException, Request, APIRouter

from prisma.models import Member
from app.models.user_schema import Member as MemberSchema

public_router = APIRouter()


@public_router.post("/test_create_member", response_model=MemberSchema)
async def test_create_member(request: MemberSchema):
    data = request.dict()
    try:
        new_member = await Member.prisma().create(
            data={
                "nickName": "john_doe",
                "email": "john@example.com",
                "password": "123456"
            }
        )
        return new_member
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
