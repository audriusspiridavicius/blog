from fastapi import APIRouter, Depends
from typing import Annotated
from blogApp.functions.login import login_user
from blogApp.database import User, get_database, Post
from blogApp.database.crud import retrieve_from_database, get_user_posts, delete_record
from sqlalchemy.orm import Session
from blogApp.pydantic import post
from typing import List


posts_router = APIRouter()

logged_user = Annotated[User, Depends(login_user)]
db = Annotated[Session, Depends(get_database)]


@posts_router.get("/posts", response_model=List[post.Post])
def get_all_posts(db:db):
    
    posts = retrieve_from_database(Post, db)
    
    return posts

@posts_router.get("/posts/{post_id}", response_model=List[post.Post])
def get_single_post(db:db, post_id:int):
    
    posts = retrieve_from_database(Post, db, id=post_id)
    
    return posts

@posts_router.get("/posts/author/{author_id}", response_model=List[post.Post])
def get_author_specific_posts(db:db, author_id:int):
    
    posts = get_user_posts(db, user_id=author_id)
    
    return posts

@posts_router.delete("/posts/{post_id}", response_model=post.Post)
def delete_post(user:logged_user,db:db, post_id:int):
    
    deleted_post = delete_record(Post, db, id=post_id, author_id=user.id)
    
    return deleted_post