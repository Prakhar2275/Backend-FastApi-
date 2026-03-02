from fastapi import FastAPI

from APP.DB.database import engine,Base

from APP.API.ROUTES import(
    auth,
    task,
    user
)

Base.metadata.create_all(
    bind=engine
)

app=FastAPI()

app.include_router(auth.router)
app.include_router(task.router)
app.include_router(user.router)



