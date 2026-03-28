
from fastapi import APIRouter
from model.register_model import Register
from controller.register_controller import register_user

registerRouter = APIRouter(prefix="/Register",tags=["Register"])

@registerRouter.post("/UserRegister")
async def create(register : Register):
    return await register_user(register)