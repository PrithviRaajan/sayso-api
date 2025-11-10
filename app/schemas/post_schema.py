from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId
from utils.objectid import PyObjectId


class PostBase(BaseModel):
    content: str

class PostCreate(PostBase):
    user_id: PyObjectId

class PostResponse(PostBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: PyObjectId
    created_at: datetime
    likes_count: Optional[int] = 0
    comments_count: Optional[int] = 0

    class Config:
        populate_by_name = True  
        json_encoders = {ObjectId: str}
        from_attributes = True  
