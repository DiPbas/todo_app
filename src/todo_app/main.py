from fastapi import FastAPI

from todo_app.routers import users, todos
from todo_app.internal.exceptions import register_exception_handlers, NotFoundError, BadRequestError

app = FastAPI()

# Registreer exceptionhandlers
register_exception_handlers(app)

app.include_router(users.router)
app.include_router(todos.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
