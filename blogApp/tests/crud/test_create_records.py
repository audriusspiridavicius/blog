from typing import List
from blogApp.database import User
import pytest
from sqlalchemy.orm import Session
from blogApp.database.crud import create
import copy
from blogApp.tests.db import get_test_database


@pytest.fixture(scope="session", autouse=True)
def db(get_test_database):
    yield get_test_database

    
@pytest.fixture
def single_user():
    user = User(username="name1", password="name1")
    return user

@pytest.fixture
def users():
    users = []
    for i in range(10):
        users.append(User(username=f"username{i}", password=f"userpass{i}"))
    return users

@pytest.fixture
def curren_user_count(db:Session):
    return db.query(User).count()

class TestCreateUser:
    
    def test_user_table_data_cleared(self,db:Session):

        db.query(User).delete()
        assert db.query(User).count()==0

        
    def test_create_single_user(self, db:Session, single_user, curren_user_count):

        created_user = create(single_user,db)
        assert created_user.username == single_user.username
        assert db.query(User).count() == curren_user_count + 1

        
    def test_create_multiple_users(self, db:Session, users:List[User], curren_user_count):

        users_count = len(users) + curren_user_count
        for user in users:
            create(user,db)

        assert db.query(User).count() == users_count
        
    def test_create_multiple_users_same_username(self, db:Session, single_user:User):
        
        second_user = copy.deepcopy(single_user)
        third_user = copy.deepcopy(single_user)
        
        
        try:
            create(single_user,db)
            create(second_user,db)
            create(third_user,db)
            assert False, "multiple users with same name should not be allowed"
        except:
            assert True