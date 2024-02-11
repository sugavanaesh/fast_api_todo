from pydantic import BaseModel 

class Model(BaseModel):
    text : str 
    is_done : bool = False