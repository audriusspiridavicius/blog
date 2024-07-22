
from .db import test_engine, TestingSessionLocal
import pytest
from sqlalchemy.orm import Session
from blogApp.database.user import User, Base

@pytest.fixture(scope="session", autouse=True)
def db():

    db = TestingSessionLocal()
    Base.metadata.create_all(bind=test_engine)
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=test_engine)

@pytest.fixture
def admin_user(db:Session):
    User.create_init_users(db)
    admin = db.query(User).filter_by(username="admin").first()
    return admin

def test_admin_user_created(db:Session):

    User.create_init_users(db)
    users = db.query(User).count()
    
    assert users == 1

@pytest.fixture
def get_password():
    return "admin"

def test_admin_password_hashed(admin_user:User, get_password):
 
    assert admin_user.verify_password(admin_user.password, get_password) == True
    
def test_admin_password_not_equal_entered_value(admin_user:User, get_password):
    
    assert admin_user.password != get_password