from datetime import datetime
from typing import Annotated
from beanie import Document, Indexed
from pydantic import Field
from bson import ObjectId
from app.models.user_model import User
from app.models.post_model import Post


class Like(Document):
    user_id: Annotated[ObjectId, Indexed()]  
    post_id: Annotated[ObjectId, Indexed()] 
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "likes"  
        indexes = [
            [("user_id", 1), ("post_id", 1)]
        ]

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "64cabc1234ef567890abcd12",
                "post_id": "64cdef1234ab567890fedc34",
                "created_at": "2025-11-10T12:00:00Z"
            }
        }
