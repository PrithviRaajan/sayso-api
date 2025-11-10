from datetime import datetime
from typing import Optional, List
from beanie import Document, Link
from pydantic import Field
from bson import ObjectId
from app.models.user_model import User
from app.models.post_model import Post


class Comment(Document):
    content: str = Field(..., max_length=300)
    user: Link[User]
    post: Link[Post]
    parent_comment_id: Optional[ObjectId] = None  # for nested replies
    created_at: datetime = Field(default_factory=datetime.utcnow)
    replies: Optional[List[ObjectId]] = Field(default_factory=list)

    class Settings:
        name = "comments"

    class Config:
        json_schema_extra = {
            "example": {
                "content": "This is a comment!",
                "user": "user_object_id",
                "post": "post_object_id",
                "parent_comment_id": None
            }
        }
