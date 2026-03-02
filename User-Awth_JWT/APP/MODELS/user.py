from sqlalchemy import Column,Integer,String,Boolean
# from pydantic import EmailStr
from APP.DB.database import Base

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True)

    email=Column(String,unique=True)

    username=Column(String,unique=True)

    hashed_password=Column(String)

    is_admin=Column(Boolean,default=False)


