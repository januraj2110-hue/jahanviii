from fastapi import APIRouter
from model.project_model import  ProjectCreateModel
from controller.project_controller import create_project, get_all_projects,update_one_project,delete_project


Projectrouter = APIRouter(prefix="/project", tags=["Projects"])


@Projectrouter.post("/add")
async def create(project: ProjectCreateModel):
    return await create_project(project)


@Projectrouter.get("/list")
async def get_projects():
    return await get_all_projects()


@Projectrouter.put("/update/{id}")
async def update_project(id:str,project:ProjectCreateModel):

    return await update_one_project(id,project)

@Projectrouter.delete("/delete/{id}")
async def delete(id:str):
    return await delete_project(id)