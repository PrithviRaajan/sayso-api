from models.post_model import Post
from schemas.post_schema import PostCreate
from bson import ObjectId
from datetime import datetime


class PostService:
    def __init__(self, db):
        self.db = db
        self.collection = db["posts"]

    async def create_post(self, post_data: PostCreate):
        post_dict = post_data.dict()
        post_dict["created_at"] = datetime.utcnow()
        post_dict["likes_count"] = 0
        post_dict["comments_count"] = 0

        result = await self.collection.insert_one(post_dict)
        return str(result.inserted_id)

    async def get_post(self, post_id: str):
        post = await self.collection.find_one({"_id": ObjectId(post_id)})
        if not post:
            raise ValueError("Post not found")
        post["id"] = str(post["_id"])
        return post

    async def get_all_posts(self):
        posts_cursor = self.collection.find({})
        posts = []
        async for post in posts_cursor:
            post["id"] = str(post["_id"])
            posts.append(post)
        return posts

    async def delete_post(self, post_id: str):
        result = await self.collection.delete_one({"_id": ObjectId(post_id)})
        if result.deleted_count == 0:
            raise ValueError("Post not found")
        return True
