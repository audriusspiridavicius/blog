from pydantic import BaseModel, ConfigDict
from typing import List, Union

class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    username:str
    
    
class UserPost(User):

    posts:Union[List['Post'], None] = None


from .post import Post