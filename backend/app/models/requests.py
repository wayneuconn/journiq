from pydantic import BaseModel


class AddUsersToGroupRequest(BaseModel):
    user_ids: list[str]
    group_id: str
