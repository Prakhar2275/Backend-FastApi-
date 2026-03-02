from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):

    email:str

    username:str

    password:str




class UserResponse(BaseModel):
    username:str

    email:str

    class Config:
        from_attribute=True


class UserOut(BaseModel):

    id:int

    email:EmailStr

    username:str

    class Config:
        from_attribute=True


