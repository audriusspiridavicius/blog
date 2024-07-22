from typing import Union
from pydantic import BaseModel, ConfigDict


class Post(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    title: str
    content: str
    
    
class PostUser(Post):

    user:'User' 
    
    
from .user import User