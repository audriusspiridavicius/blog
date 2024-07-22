from fastapi import FastAPI
from fastapi.security import HTTPBasic
from .database import database, user


app = FastAPI()

auth = HTTPBasic()

from .routes import users
app.include_router(users.router)