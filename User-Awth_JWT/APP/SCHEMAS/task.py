from pydantic import BaseModel

class TaskCreate(BaseModel):
    title:str

    description:str

class TaskOut(BaseModel):

    id:int
    title:str
    desription:str
    completed:bool

    class Config:
        from_attribute:True

    
