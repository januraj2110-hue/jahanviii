from dbconnect import task_collection
from model.task_model import Task
from bson import ObjectId

async def create_task(task: Task):
    result = await task_collection.insert_one(task.dict())
    return {"message": "Task created successfully"}

async def get_all_tasks():  
    try:
        cursor = task_collection.find()
        x = []
        async for i in cursor:
            i["_id"] = str(i["_id"])
            x.append(i)
        return {"tasks": x}
    except Exception as e:
        # If there is a database connection error, it will show here
        return {"error": str(e)}
    
async def update_one_task(task_id: str, task: Task):
    result = await task_collection.update_one(
        {"_id": ObjectId(task_id)},
          {"$set": task.dict()})
    if result.modified_count == 1:
        return {"message": "Task updated successfully"}
    else:
        return {"message": "Task not found or no changes made"}
    
async def delete_one_task(task_id: str):
    result = await task_collection.delete_one(
        {"_id": ObjectId(task_id)})
    if result.deleted_count == 1:
        return {"message": "Task deleted successfully"}
    else:
        return {"message": "Task not found"}