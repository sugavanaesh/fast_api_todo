from fastapi import FastAPI
import uvicorn
from db.connection import connection,engine,session
from db.table import Todo
from model.model import Model

app = FastAPI()
connection()
Todo.metadata.create_all(engine)


@app.get("/")
def home():
    return{"msg":"I'M FAST"}

@app.post("/insertTodo")
async def insert(payload : Model):
    data = Todo(**payload.model_dump())
    session.add(data)
    session.commit()
    # session.close()
    return {"Todo added":data.text}

@app.get("/all")
async def get_all():
    data = session.query(Todo)
    return data.all()


@app.put("/update/{id}")
async def update(
    id:int,
    new_text:str="",
    is_complete:bool = False
):
    todo_query = session.query(Todo).filter(Todo.id==id)
    res = todo_query.first()
    if new_text:
        res.text = new_text
    res.is_done = is_complete
    session.add(res)
    session.commit()

if __name__ == "__main__":
    uvicorn.run("server:app",reload=True)