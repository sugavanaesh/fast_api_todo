from sqlalchemy import Column,String,Integer,Boolean 
from .connection import base 

class Todo(base):
    __tablename__ = "todos"

    id = Column(Integer,primary_key=True)
    text = Column(String)
    is_done = Column(Boolean,default=False)