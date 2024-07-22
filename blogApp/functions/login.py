from typing import Annotated
from fastapi.security import HTTPBasicCredentials
from fastapi import Depends
from blogApp.app import auth
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException

from blogApp.database.get_database import get_database

def login_user(creditials:Annotated[HTTPBasicCredentials, Depends(auth)], db:Annotated[Session, Depends(get_database)]):
    """Login user"""
    from blogApp.database.user import User
    logged_user = User.login(username=creditials.username, password=creditials.password, db=db)
    if logged_user:
        return logged_user
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")
