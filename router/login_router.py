
from fastapi import APIRouter
from model.login_model import Login
from controller.login_controller import User_login

LoginRouter= APIRouter(prefix="/Login", tags=["Login"])

@LoginRouter.post("/")
async def User(login : Login):
    return await User_login(login)
    
