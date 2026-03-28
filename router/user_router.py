
from fastapi import APIRouter
from model.user_model import User
from controller.user_controller import create_user, get_all_users,update_one_user,delete_user


Userrouter = APIRouter(prefix="/users", tags=["Users"])


@Userrouter.post("/")
async def create(user: User):
    return await create_user(user)


@Userrouter.get("/list")
async def get_user():
    return await get_all_users()


@Userrouter.put("/update/{id}")
async def update_user(id:str,User:User):
    return await update_one_user(id,User)

@Userrouter.delete("/delete/{id}")
async def delete(id:str):   
    return await delete_user(id)
