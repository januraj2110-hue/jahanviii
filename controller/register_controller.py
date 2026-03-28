
from dbconnect import register_collection
from model.register_model import Register
# from bson import ObjectID
from bcryptEx import *

async def register_user(register: Register):
    try:
        hashed_password = hash_password(register.password)
        register.password = hashed_password

        result = await register_collection.insert_one(register.dict())

        if result.inserted_id:
            return {"message": "User registered successfully"}
        else:
            return {"message": "User registration failed"}
    except Exception as e:
        return {"error": str(e)}