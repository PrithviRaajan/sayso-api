from fastapi import APIRouter, Depends, HTTPException
from schemas.user_schema import UserCreate
from services.user_service import UserService
from core.db import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", summary="Create a new user")
async def create_user(user_data: UserCreate, db=Depends(get_db)):
    service = UserService(db)
    try:
        user_id = await service.create_user(user_data)
        return {"message": "User created successfully", "user_id": user_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", summary="Get all users")
async def get_users(db=Depends(get_db)):
    service = UserService(db)
    users = await service.get_all_users()
    return {"users": users}


@router.get("/{user_id}", summary="Get user by ID")
async def get_user(user_id: str, db=Depends(get_db)):
    service = UserService(db)
    try:
        user = await service.get_user(user_id)
        return user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
