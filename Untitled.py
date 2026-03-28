
from fastapi import APIRouter, HTTPException, Query
from model.project_model import *
from dbconnect import project_collection
from datetime import datetime
from bson import ObjectId
from typing import Optional, List

router = APIRouter(prefix="/api/projects", tags=["Projects"])

# Collections Reference
project_collection = project_collection("projects")
task_collection = database.get_collection("tasks")

@router.post("")
async def create_project(project: ProjectCreate):
    """
    Naya project create karta hai aur initial tasks ko 
    task collection mein distribute karta hai.
    """
    try:
        project_dict = project.model_dump()
        project_dict["createdAt"] = datetime.utcnow()
        
        # Ensure creator is in members
        if "memberIds" not in project_dict or not project_dict["memberIds"]:
            project_dict["memberIds"] = [project.createdBy]
        elif project.createdBy not in project_dict["memberIds"]:
            project_dict["memberIds"].append(project.createdBy)

        # 1. Project ki initial tasks ko buffer mein lena aur main doc se hatana
        initial_tasks = project_dict.pop("tasks", [])
        
        # 2. Project document save karna
        result = await project_collection.insert_one(project_dict)
        project_id = str(result.inserted_id)

        # 3. Agar initial tasks list mein hain, toh unhe 'tasks' collection mein save karna
        if initial_tasks:
            tasks_payload = []
            for t in initial_tasks:
                # 't' yahan ProjectTask model ka dictionary format hai
                tasks_payload.append({
                    "name": t.get("title") or t.get("name"),
                    "description": t.get("description", ""),
                    "priority": t.get("priority", "Medium"),
                    "status": t.get("status", "In progress"),
                    "projectId": project_id, # Linking reference
                    "projectName": project.name,
                    "createdBy": project.createdBy,
                    "createdAt": datetime.utcnow(),
                    "assignee": "Unassigned"
                })
            
            if tasks_payload:
                await task_collection.insert_many(tasks_payload)

        return {
            "status": "success", 
            "id": project_id,
            "message": f"Mission {project.name} initialized with {len(initial_tasks)} assets."
        }
    except Exception as e:
        print(f"Error in Project Creation: {e}")
        raise HTTPException(status_code=500, detail="Failed to initialize project")

@router.get("")
async def get_projects(user_id: Optional[str] = Query(None)):
    """
    User ke projects fetch karta hai aur '$lookup' use karke 
    real-time 'taskCount' populate karta hai.
    """
    try:
        if not user_id:
            return []

        # Population (Aggregation) Pipeline
        pipeline = [
            # Step 1: User ke membership wale projects filter karo
            {"$match": {"memberIds": user_id}},
            
            # Step 2: Tasks collection se join (Population)
            {
                "$lookup": {
                    "from": "tasks",
                    "let": {"current_pid": {"$toString": "$_id"}}, # _id ko string mein convert kiya
                    "pipeline": [
                        # Sirf wahi tasks match karega jinka projectId match ho
                        {"$match": {"$expr": {"$eq": ["$projectId", "$$current_pid"]}}}
                    ],
                    "as": "linked_missions"
                }
            },
            
            # Step 3: Count calculate karke naya field add karna
            {
                "$addFields": {
                    "taskCount": {"$size": "$linked_missions"}
                }
            },
            
            # Step 4: Sorting (Latest projects first)
            {"$sort": {"createdAt": -1}},
            
            # Step 5: Clean up (Extra data ko response se hatana)
            {
                "$project": {
                    "linked_missions": 0 # Tasks list nahi chahiye, sirf count chahiye
                }
            }
        ]

        projects = []
        async for doc in project_collection.aggregate(pipeline):
            doc["_id"] = str(doc["_id"])
            projects.append(doc)
            
        return projects
    except Exception as e:
        print(f"Error in Fetching Projects: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/{project_id}")
async def delete_project(project_id: str):
    """
    Project aur usse linked saari tasks ko delete karna (Cleanup logic)
    """
    try:
        # Delete Project
        p_res = await project_collection.delete_one({"_id": ObjectId(project_id)})
        # Delete linked tasks
        t_res = await task_collection.delete_many({"projectId": project_id})
        
        return {
            "status": "success", 
            "message": f"Project deleted. {t_res.deleted_count} tasks purged."
        }
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID or deletion failed")
    
    
    
    
