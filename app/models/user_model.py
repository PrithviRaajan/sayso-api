from typing import Annotated
from beanie import Document, Indexed
from pydantic import EmailStr, Field
from datetime import datetime

class User(Document):
    username: Annotated[str, Indexed(unique=True)]
    email: Annotated[EmailStr, Indexed(unique=True)]
    password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "users"

    class Config:
        json_schema_extra = {
            "example": {
                "username": "prithvi",
                "email": "prithvi@example.com",
                "password": "hashed_password_here"
            }
        }
