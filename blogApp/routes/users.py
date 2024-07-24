from typing import Annotated, List
from fastapi import Depends

from blogApp.database import get_database
from blogApp.functions.login import login_user
from fastapi import APIRouter

from blogApp.database.user import User
from blogApp import pydantic
from blogApp.database.crud import retrieve_from_database
from sqlalchemy.orm import Session

router = APIRouter()



@router.post("/users", response_model=pydantic.User)
def user(user:Annotated[User, Depends(login_user)]):
    
    return user

@router.post("/users/{user_id}", response_model=List[pydantic.User])
def user(user_id, db:Annotated[Session, Depends(get_database)]):
    
    return retrieve_from_database(User,db,id=user_id)