from fastapi import APIRouter
from model.team_model import TeamCreate, TeamUpdate, TeamResponse
from controller.team_controller import create_team, get_all_teams, get_team_by_id, update_team, delete_team


TeamRouter = APIRouter(
    prefix="/team",
    tags=["team"]
)

@TeamRouter.post("/add")
async def create(team: TeamCreate):
    return await create_team(team)

@TeamRouter.get("/list")
async def get_teams():
    return await get_all_teams()

@TeamRouter.get("/{team_id}")
async def get_team(team_id: str):
    return await get_team_by_id(team_id)

@TeamRouter.put("/{team_id}")
async def update(team_id: str, team: TeamUpdate):
    return await update_team(team_id, team)

@TeamRouter.delete("/{team_id}")
async def delete(team_id: str):
    return await delete_team(team_id)
