#  creating the task routes
from fastapi import FastAPI,APIRouter,Depends,HTTPException

from sqlalchemy.orm import Session

from APP.MODELS.task import Task

from APP.SCHEMAS.task import TaskCreate,TaskOut

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

@router.get("/")
def get_task_api(
    db:Session=Depends(get_db),
    current_user:User=Depends(get_current_user)
):
    return get_task(
        db,
        current_user.id
    )


#  UPDATE TASK
@router.put("/{task_id}", response_model=TaskOut)
def update_task(
    task_id: int,
    updated_task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == current_user.id
    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = updated_task.title
    task.description = updated_task.description

    db.commit()
    db.refresh(task)

    return task


# DELETE TASK
@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == current_user.id
    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully"}