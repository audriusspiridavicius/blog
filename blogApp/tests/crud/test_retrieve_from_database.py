from blogApp.database.crud import retrieve_from_database
from blogApp.database import Post, User
import pytest
from blogApp.tests.db import get_test_database
from sqlalchemy.orm import Session

@pytest.fixture
def db(get_test_database):
    yield get_test_database

class TestRetrieveModelFromDatabase:
    

    def test_get_existing_user(self, db:Session):
        
        users = retrieve_from_database(User, db, id=1)
        assert len(users) == 1
    
    def test_get_all_users(self, db:Session):
        
        users = retrieve_from_database(User, db)
        assert len(users) == db.query(User).count()
        
    def test_get_non_existing_user(self, db:Session):
        
        users = retrieve_from_database(User, db, id=99999999)
        assert len(users) == 0
        
    @pytest.mark.parametrize("model,properties",[(User,{"name":1}), (Post, {"address":"address"})])
    def test_non_existing_property(self, db:Session, model, properties):
        
        users = retrieve_from_database(model, db, **properties)
        
        assert len(users) == db.query(User).count()
        
    @pytest.mark.parametrize("model,properties",[(User,{"id":1, "email":"test@testtestemail.com"})])
    def test_mixed_properties(self, db:Session, model, properties):
        
        users = retrieve_from_database(model, db, **properties)
        assert len(users) == 1