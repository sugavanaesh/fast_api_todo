from pydantic import BaseModel 

class Model(BaseModel):
    text : str 
    is_done : bool = False

class UpdateModel(BaseModel):
    id:int
    new_text:str=""
    is_complete:bool = False