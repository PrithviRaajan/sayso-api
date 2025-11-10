from bson import ObjectId
from datetime import datetime


class InteractionService:
    def __init__(self, db):
        self.db = db
        self.likes = db["likes"]
        self.posts = db["posts"]

    async def like_post(self, user_id: str, post_id: str):
        existing_like = await self.likes.find_one({"user_id": user_id, "post_id": post_id})
        if existing_like:
            raise ValueError("Already liked")

        await self.likes.insert_one({
            "user_id": user_id,
            "post_id": post_id,
            "created_at": datetime.utcnow()
        })

        await self.posts.update_one({"_id": ObjectId(post_id)}, {"$inc": {"likes_count": 1}})
        return {"message": "Post liked"}

    async def unlike_post(self, user_id: str, post_id: str):
        result = await self.likes.delete_one({"user_id": user_id, "post_id": post_id})
        if result.deleted_count == 0:
            raise ValueError("Like not found")

        await self.posts.update_one({"_id": ObjectId(post_id)}, {"$inc": {"likes_count": -1}})
        return {"message": "Post unliked"}

    async def get_likes(self, post_id: str):
        count = await self.likes.count_documents({"post_id": post_id})
        return {"likes_count": count}
