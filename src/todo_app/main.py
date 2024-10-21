from fastapi import FastAPI
from .sqlmodel_orm.models import *
from .routers import users, todos


app = FastAPI()

app.include_router(users.router)
app.include_router(todos.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
