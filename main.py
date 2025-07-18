from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/todos")
def read_root():
    return {"Hello": "World"}


@app.post("/todos")
def create_todo(todo: dict):
    return {"todo": todo}


@app.get("/todos/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/todos/{item_id}")
def update_item(item_id: int, todo: dict):
    return {"item_id": item_id, "todo": todo}


@app.delete("/todos/{item_id}")
def delete_item(item_id: int):
    return {"item_id": item_id, "status": "deleted"}
