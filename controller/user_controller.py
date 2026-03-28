from dbconnect import user_collection
from model.user_model import User
from bson import ObjectId

async def create_user(user: User):
    result = await user_collection.insert_one(user.dict())
    return {"message": "User created successfully"}
    
async def get_all_users():  # You might want to rename this to get_all_users for clarity
    try:
        cursor = user_collection.find()
        x = []
        async for i in cursor:
            i["_id"] = str(i["_id"])
            x.append(i)
        return {"users": x}
    except Exception as e:
        # If there is a database connection error, it will show here
        return {"error": str(e)}
    
async def update_one_user(id: str, Users: User):
    try:
        result = await user_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": Users.dict()}
        )
        if result.modified_count == 1:
            return {"message":"User Updated"}
        else:
            return{"message":"no changes are made!!"}

    except Exception as e:
        print(e)
        return {"error": str(e)}
    
async def delete_user(id :str):
    try:
        result = await user_collection.delete_one({"_id": ObjectId(id)})
        return {"Message":"success"}
    except Exception as e:
        return {"exception":e}
