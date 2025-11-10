from datetime import datetime
from pydantic import BaseModel, Field
from bson import ObjectId
from schemas.user_schema import PyObjectId

class LikeBase(BaseModel):
    user_id: PyObjectId
    post_id: PyObjectId


class LikeResponse(LikeBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    created_at: datetime

    class Config:
        populate_by_name = True  # allows _id <-> id mapping
        json_encoders = {ObjectId: str}
        from_attributes = True  # replaces orm_mode in Pydantic v2
