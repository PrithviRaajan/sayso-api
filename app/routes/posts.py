from fastapi import APIRouter, Depends, HTTPException
from app.schemas.post_schema import PostCreate
from app.services.post_service import PostService
from app.core.db import get_db

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/", summary="Create a post")
async def create_post(post_data: PostCreate, db=Depends(get_db)):
    service = PostService(db)
    try:
        post_id = await service.create_post(post_data)
        return {"message": "Post created successfully", "post_id": post_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", summary="List all posts")
async def list_posts(db=Depends(get_db)):
    service = PostService(db)
    posts = await service.get_all_posts()
    return {"posts": posts}


@router.get("/{post_id}", summary="Get a single post")
async def get_post(post_id: str, db=Depends(get_db)):
    service = PostService(db)
    try:
        post = await service.get_post(post_id)
        return post
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{post_id}", summary="Delete a post")
async def delete_post(post_id: str, db=Depends(get_db)):
    service = PostService(db)
    try:
        await service.delete_post(post_id)
        return {"message": "Post deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
