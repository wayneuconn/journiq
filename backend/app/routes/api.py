# backend/app/routes/api.py
from fastapi import APIRouter, Depends
from google.cloud import firestore

from app.core.config import credentials, settings
from app.models.schema import Member, Group, TravelPlanner, GroupItem, PersonalItem, Payment

router = APIRouter()

# Dependency function to provide Firestore client
def get_firestore_client():
    return firestore.Client(credentials=credentials, project=settings.FIREBASE_PROJECT_ID)

@router.get("/members/")
async def list_members(firestore_client: firestore.Client = Depends(get_firestore_client)):
    members_ref = firestore_client.collection("members")
    docs = members_ref.stream()
    members = [doc.to_dict() for doc in docs]
    return {"members": members}


@router.post("/members/")
async def create_member(member: Member):
    doc_ref = firestore_client.collection("members").document(member.memberUID)
    doc_ref.set(member.dict())
    return {"status": "member created"}


@router.post("/groups/")
async def create_group(group: Group):
    doc_ref = firestore_client.collection("groups").document(group.groupUID)
    doc_ref.set(group.dict())
    return {"status": "group created"}


@router.post("/travel_planner/")
async def create_travel_planner(planner: TravelPlanner):
    doc_ref = firestore_client.collection("travelPlanners").document(planner.planner_id)
    doc_ref.set(planner.dict())
    return {"status": "travel planner created"}


@router.post("/items/group/")
async def create_group_item(item: GroupItem):
    doc_ref = firestore_client.collection("items").document("groupItems").collection("groupItems").document(
        item.item_id)
    doc_ref.set(item.dict())
    return {"status": "group item created"}


@router.post("/items/personal/")
async def create_personal_item(item: PersonalItem):
    doc_ref = firestore_client.collection("items").document("personalItems").collection("personalItems").document(
        item.item_id)
    doc_ref.set(item.dict())
    return {"status": "personal item created"}


@router.post("/payments/")
async def create_payment(payment: Payment):
    doc_ref = firestore_client.collection("payments").document(payment.payment_id)
    doc_ref.set(payment.dict())
    return {"status": "payment created"}
