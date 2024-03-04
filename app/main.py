from fastapi import FastAPI
from . import models
from .database import engine
from .routers import miniature, user, auth

app = FastAPI()

app.include_router(miniature.router)
app.include_router(user.router)
app.include_router(auth.router)

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def root() -> str:
    return "Hello world! I'm alive!"
