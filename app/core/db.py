from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from contextlib import asynccontextmanager
from core.config import settings

from models.user_model import User
from models.post_model import Post
from models.comment_model import Comment
from models.like_model import Like

client = None
db = None

async def connect_to_mongo():
    global client, db
    client = AsyncIOMotorClient(settings.MONGO_URI, maxPoolSize=10, minPoolSize=1)
    db = client[settings.DB_NAME]

    await init_beanie(
        database=db,
        document_models=[User, Post, Comment, Like],
    )

    print(f"✅ Connected to MongoDB Atlas: {settings.DB_NAME}")

async def close_mongo_connection():
    global client
    if client:
        client.close()
        print("❌ MongoDB connection closed.")


@asynccontextmanager
async def get_db():
    try:
        yield db
    finally:
        pass
