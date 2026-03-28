from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class TeamCreate(BaseModel):
    name: str
    projectId: str
    memberIds: List[str]
    createdBy: str

class TeamUpdate(BaseModel):
    name: Optional[str] = None
    projectId: Optional[List[str]] = None
    memberIds: Optional[List[str]] = None

class TeamResponse(BaseModel):
    id: str
    name: str
    projectId: str
    memberIds: List[str]
    createdBy: str
    createdAt: datetime
    updatedAt: datetime