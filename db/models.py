from db.database import Base
from sqlalchemy import Column, String, Integer, Boolean



class TasksDB(Base):
    __tablename__="tasks"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    is_completed = Column(Boolean,default=False)

