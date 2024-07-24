import pytest
from blogApp.database.user import User, Base
from blogApp.database.post import Post
from blogApp.database.crud import create
from sqlalchemy.orm import Session
from .db import TestingSessionLocal, test_engine
from sqlalchemy.exc import IntegrityError

@pytest.fixture(scope="function", autouse=True)
def db():

    db = TestingSessionLocal()
    Base.metadata.create_all(bind=test_engine)
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=test_engine)

    
@pytest.fixture
def user():
    
    return User(username="user123", password="user123")

@pytest.fixture
def post(user):
    
    p = Post()
    p.author = user
    p.content = "test post content"
    p.title = " post title"
    
    return p

@pytest.fixture
def postwithoutuser():
    
    p = Post()
    p.content = "test post content"
    p.title = " some random title"
    
    return p


class TestPostCreateWithUser:
    
    def test_post_saved(self, post:Post, db:Session):
        
        saved_post:Post = create(post, db)
        assert db.query(Post).count() == 1
        
    def test_author_assigned(self, post:Post, db:Session):
        
        saved_post:Post = create(post, db)
        assert saved_post.author_id == 1
    
    def test_author_correct_name(self, post:Post, db:Session, user:User):
        
        saved_post:Post = create(post, db)
        assert saved_post.author.username == user.username


class TestPostCreateWithouthUserSet:
    
    def test_save_post(self, postwithoutuser:Post, db:Session):
        
        try:
            saved_post = create(postwithoutuser, db)
        except IntegrityError:
            assert True, "Should throw an error because author of post is not set"