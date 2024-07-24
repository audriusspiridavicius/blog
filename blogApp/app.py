from fastapi import FastAPI
from fastapi.security import HTTPBasic
from .database import database, user, get_database
from .tests.db import get_test_database

app = FastAPI()

auth = HTTPBasic()

from .routes import users
app.include_router(users.router)
app.dependency_overrides[get_database] = get_test_database