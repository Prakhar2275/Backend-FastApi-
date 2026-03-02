from APP.MODELS.task import Task

def create_task(db,title,description,owner_id):
    task=Task(
        title=title,
        description=description,
        owner_id=owner_id
    )
    

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def get_task(db,owner_id:int):
    tasks=db.qurey(Task).filter(
        Task.owner_id==owner_id
    ).all()

    return tasks
    
