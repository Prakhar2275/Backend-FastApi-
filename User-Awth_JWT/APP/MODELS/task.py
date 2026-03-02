from sqlalchemy import Integer,String,Column,Boolean

from APP.DB.database import Base

class Task(Base):
    __tablename__="task"

    id=Column(Integer,primary_key=True)

    title=Column(String)

    description=Column(String)

    completed=Column(Boolean)