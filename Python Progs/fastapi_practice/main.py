from http.client import HTTPException
from typing import List
from uuid import uuid4, UUID

from fastapi import FastAPI
from models import User, Gender, Role, UserUpdate

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("6ffd4b32-21ca-4499-b182-2259b6909a85"),
        first_name="Vi",
        last_name="D",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("1e1f28c7-bcb9-4fad-8e34-bb7d8bb24df3"),
        first_name="Alex",
        last_name="X",
        gender=Gender.male,
        roles=[Role.user, Role.admin]
    )
]


@app.get("/")
async def root():
    print("Root endpoint hit")
    return {"Hello": "Vi"}


@app.get("/api/v1/users")
async def fetch_users():
    print("Fetching Users")
    return db


@app.post("/api/v1/users")
async def reg_users(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def del_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return

    raise HTTPException(status_code=404,detail=f"user id : {user_id} does not exists.")


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdate, user_id: UUID):
    for user in db:
        if user_update.first_name is not None:
            user.first_name = user_update.first_name
        if user_update.last_name is not None:
            user.last_name = user_update.last_name
        if user_update.middle_name is not None:
            user.middle_name = user_update.middle_name
        if user_update.roles is not None:
            user.roles = user_update.roles
        return
    raise HTTPException(status_code=404, detail=f"user id: {user_id} doesn't exist")
