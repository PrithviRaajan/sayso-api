from datetime import datetime
from typing import Optional, List
from beanie import Document, Link
from pydantic import Field
from bson import ObjectId
from app.models.user_model import User


class Post(Document):
    content: str = Field(..., max_length=280)
    author: Link[User]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    likes_count: int = Field(default=0)
    comments: Optional[List[ObjectId]] = Field(default_factory=list)

    class Settings:
        name = "posts"

    class Config:
        json_schema_extra = {
            "example": {
                "content": "This is my first post!",
                "author": "user_object_id",
                "likes_count": 0
            }
        }
