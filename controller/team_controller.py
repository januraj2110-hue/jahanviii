from dbconnect import team_collection
from model.team_model import TeamCreate, TeamUpdate, TeamResponse
from bson import ObjectId

async def create_team(team: TeamCreate):
    result = await team_collection.insert_one(team.dict())
    return {"message": "Team created successfully"}

async def get_all_teams():  
    try:
        cursor = team_collection.find()
        x = []
        async for i in cursor:
            i["_id"] = str(i["_id"])
            x.append(i)
        return {"teams": x}
    except Exception as e:
        # If there is a database connection error, it will show here
        return {"error": str(e)} 
    
async def get_team_by_id(team_id: str):
    try:
        team = await team_collection.find_one({"_id": ObjectId(team_id)})
        if team:
            team["_id"] = str(team["_id"])
            return {"team": team}
        else:
            return {"message": "Team not found"}
    except Exception as e:

        return {"error": str(e)}
    
async def update_team(team_id: str, team: TeamUpdate):
    try:
        result = await team_collection.update_one(
            {"_id": ObjectId(team_id)},
            {"$set": team.dict()}
        )
        if result.modified_count > 0:
            return {"message": "Team updated successfully"}
        else:
            return {"message": "Team not found or no changes made"}
    except Exception as e:
        
        return {"error": str(e)}
    
async def delete_team(team_id: str):
    try:
        result = await team_collection.delete_one({"_id": ObjectId(team_id)})
        if result.deleted_count > 0:
            return {"message": "Team deleted successfully"}
        else:
            return {"message": "Team not found"}
    except Exception as e:
        
        return {"error": str(e)}