from fastapi import FastAPI
import uvicorn
from db.connection import connection, engine, session
from db.table import Todo
from model.model import Model, UpdateModel

app = FastAPI()
connection()
Todo.metadata.create_all(engine)


@app.get("/")
def home():
    return {"msg": "I'M FAST"}


@app.post("/insertTodo")
async def insert(payload: Model):
    data = Todo(**payload.model_dump())
    session.add(data)
    session.commit()
    # session.close()
    return {"Todo added": data.text}


@app.get("/all")
async def get_all():
    data = session.query(Todo)
    return data.all()


@app.put("/update/{id}")
async def update(payload: UpdateModel):
    todo_query = session.query(Todo).filter(Todo.id == payload.id)
    res = todo_query.first()
    if payload.new_text:
        res.text = payload.new_text
    if payload.is_complete:
        res.is_done = True
    res.is_done = payload.is_complete
    session.add(res)
    session.commit()


@app.delete("/{id}")
async def delete(id):
    todo_query = session.query(Todo).filter(Todo.id == id).first()
    print(todo_query)
    session.delete(todo_query)
    session.commit()



if __name__ == "__main__":
    uvicorn.run("server:app", reload=True)
