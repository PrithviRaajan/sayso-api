from fastapi import FastAPI
from routes import users, posts, interactions
from core.db import connect_to_mongo, close_mongo_connection

app = FastAPI(title="SaySo")

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(interactions.router)


@app.on_event("startup")
async def startup_db():
    await connect_to_mongo()


@app.on_event("shutdown")
async def shutdown_db():
    await close_mongo_connection()
