#  creating the task routes
from fastapi import FastAPI,APIRouter,Depends

from sqlalchemy.orm import Session

from APP.SCHEMAS.task import TaskCreate

from APP.CRUD.task import(
    create_task,
    get_task
)


from APP.API.desp import get_db

from APP.CORE.dependecies import get_current_user


from APP.MODELS.user import User

router=APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

# creating the first task

@router.post("/")
def create_task_api(
    task:TaskCreate,
    db:Session=Depends(get_db),
    current_user:User=Depends(get_current_user)
):
    return create_task(
        db,
        task.title,
        task.descrption,
        current_user.id
    )


#  getting the task form the table

@router.post("/")
def get_task_api(
    db:Session=Depends(get_db),
    current_user:User=Depends(get_current_user)
):
    return get_task(
        db,
        current_user.id
    )