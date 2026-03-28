from fastapi import APIRouter
from model.task_model import Task
from controller.task_controller import create_task, get_all_tasks, update_one_task, delete_one_task

Taskrouter = APIRouter(prefix="/task", tags=["Tasks"])

@Taskrouter.post("/add")
async def create(task: Task):
    return await create_task(task)

@Taskrouter.get("/list")
async def get_tasks():
    return await get_all_tasks()

@Taskrouter.put("/update/{task_id}")
async def update_task(task_id: str, task: Task):
    return await update_one_task(task_id, task)

@Taskrouter.delete("/delete/{task_id}")
async def delete_task(task_id: str):
    return await delete_one_task(task_id)
