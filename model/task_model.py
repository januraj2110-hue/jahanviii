from pydantic import BaseModel

class Task(BaseModel):
    taskname: str
    description: str

    priority: int

    