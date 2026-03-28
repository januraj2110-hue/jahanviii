from dbconnect import project_collection
from model.project_model import  ProjectCreateModel
from bson import ObjectId

async def create_project(project: ProjectCreateModel):
    result = await project_collection.insert_one(project.dict()) 
    return {"message": "Project created successfully"}

async def get_all_projects():  # You might want to rename this to get_all_projects for clarity
    try:
        cursor = project_collection.find()
        x = []
        async for i in cursor:
            i["_id"] = str(i["_id"])
            x.append(i)
        return {"projects": x}
    except Exception as e:
        # If there is a database connection error, it will show here
        return {"error": str(e)}
    
async def update_one_project(id: str, project: ProjectCreateModel):
    try:
        result = await project_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": project.dict()}
        )
        if result.modified_count == 1:
            return {"message":"Project Updated"}
        else:
            return{"message":"no changes are made!!"}

    except Exception as e:
        print(e)
        return {"error": str(e)}
    
async def delete_project(id:str):
    try:
        result = await project_collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 1:
            return {"message":"Project Deleted"}
        else:
            return{"message":"Project not found!!"}

    except Exception as e:
        print(e)
        return {"error": str(e)}