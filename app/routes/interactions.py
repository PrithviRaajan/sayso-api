from fastapi import APIRouter, Depends, HTTPException
from app.services.interaction_service import InteractionService
from app.core.db import get_db

router = APIRouter(prefix="/interactions", tags=["Interactions"])


@router.post("/like/{post_id}", summary="Like a post")
async def like_post(user_id: str, post_id: str, db=Depends(get_db)):
    service = InteractionService(db)
    try:
        return await service.like_post(user_id, post_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/unlike/{post_id}", summary="Unlike a post")
async def unlike_post(user_id: str, post_id: str, db=Depends(get_db)):
    service = InteractionService(db)
    try:
        return await service.unlike_post(user_id, post_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/likes/{post_id}", summary="Get like count for a post")
async def get_likes(post_id: str, db=Depends(get_db)):
    service = InteractionService(db)
    return await service.get_likes(post_id)
