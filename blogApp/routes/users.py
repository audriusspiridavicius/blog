from typing import Annotated
from fastapi import Depends

from blogApp.functions.login import login_user
from fastapi import APIRouter

from blogApp.database.user import User
from blogApp import pydantic


router = APIRouter()



@router.post("/users", response_model=pydantic.User)
def user(user:Annotated[User, Depends(login_user)]):
    
    return user