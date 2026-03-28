from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(
    "mongodb+srv://jahanvi:jahanvi2108@cluster0.1etnzrl.mongodb.net/?appName=Cluster0")

db = client["register_db"]
register_collection = db["register"]
login_collection = db["login"]
user_collection = db["user"]
project_collection = db["project"]
task_collection = db["task"]
team_collection = db["team"]