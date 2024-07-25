from fastapi import FastAPI
from fastapi.security import HTTPBasic
from .database import database, user, get_database
from .tests.db import test_database

app = FastAPI()

auth = HTTPBasic()

from .routes import users
from .routes import posts

app.include_router(users.router)
app.include_router(posts.posts_router)

app.dependency_overrides[get_database] = test_database