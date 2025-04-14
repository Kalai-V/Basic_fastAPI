from fastapi import APIRouter
from .schemas import User
from .models import add_user, get_all_users
from typing import List

router = APIRouter()

@router.post("/submit/")
def submit_user(user: User):
    add_user(user.dict())
    return {"user":user,"message":"Data logged successfully" }

@router.get("/user/", response_model=List[User])
def get_users():
    return get_all_users()