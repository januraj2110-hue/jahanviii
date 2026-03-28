
from fastapi import FastAPI
from router.register_router import registerRouter
from router.login_router import LoginRouter
from router.user_router import Userrouter
from router.project_router import Projectrouter
from router.task_router import Taskrouter
from router.team_router import TeamRouter

app = FastAPI(title="TaskHive API", description="API for TaskHive application") 
app.include_router(registerRouter)
app.include_router(LoginRouter)
app.include_router(Userrouter)
app.include_router(Projectrouter)
app.include_router(Taskrouter)
app.include_router(TeamRouter)

