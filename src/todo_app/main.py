from fastapi import FastAPI, Query, HTTPException
from typing import List, Annotated
from sqlmodel import select
from .sqlmodel_orm.models import *
from .dependencies import SessionDep
from .routers import users, todos


app = FastAPI()

app.include_router(users.router)
app.include_router(todos.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
