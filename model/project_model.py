from typing import List, Optional
from pydantic import BaseModel

class TaskModel(BaseModel):
     title: str
     priority: Optional[str] = "medium"
     status: Optional[str] = "in progress"

class ProjectCreateModel(BaseModel):
    name: str
    description: Optional[str] 
    tasks: List[TaskModel] 
    createdBy: list[str]



