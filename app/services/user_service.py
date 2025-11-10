from models.user_model import User
from schemas.user_schema import UserCreate
from passlib.context import CryptContext
from bson import ObjectId

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    def __init__(self, db):
        self.db = db
        self.collection = db["users"]

    async def create_user(self, user_data: UserCreate):
        existing_user = await self.collection.find_one({"email": user_data.email})
        if existing_user:
            raise ValueError("User already exists")

        hashed_password = pwd_context.hash(user_data.password)
        user_dict = user_data.dict()
        user_dict["password"] = hashed_password

        result = await self.collection.insert_one(user_dict)
        return str(result.inserted_id)

    async def get_user(self, user_id: str):
        user = await self.collection.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise ValueError("User not found")
        user["id"] = str(user["_id"])
        return user

    async def get_all_users(self):
        users_cursor = self.collection.find({})
        users = []
        async for user in users_cursor:
            user["id"] = str(user["_id"])
            users.append(user)
        return users
