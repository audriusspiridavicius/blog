import pytest
from ..db import get_test_database
from blogApp.database import User, Post
from blogApp.database.crud import retrieve_from_database, delete_record
from sqlalchemy.orm import Session

@pytest.fixture(scope="module")
def db(get_test_database):
    return get_test_database


@pytest.fixture(autouse=True, scope="class")
def set_up_database_records(db:Session):

    users = [User(username=f'test{i}', password='test{i}') for i in range(5,10)]
    db.add_all(users)
    db.commit()
    
    
    post = Post(title="test post", content="test content value", author_id=5)
    db.add(post)
    db.commit()


class TestDeleteFromDatabaseFunction:
    
    
    @pytest.mark.parametrize("model, id",[(User, 1), (User, 2), (User, 3), (User, 4), (Post, 1)])
    def test_delete_successfully(self, db, model, id):
        
        delete_record(model, db, id)
        after_delete_count = len(retrieve_from_database(model, db, id=id))
        
        assert after_delete_count == 0
    
    @pytest.mark.parametrize("model, id",[(User, 100), (User, 0), (User, 99999), (User, 888), (Post, 9)])
    def test_delete_non_existing_record(self, db, model, id):
        
        deleted = delete_record(model, db, id)
        assert deleted == None
    
    @pytest.mark.parametrize("model, id",[(User, 1), (User, 2), (User, 3), (User, 4), (Post, 1)])
    def test_delete_existing_record(self, db, model, id):
        
        deleted = delete_record(model, db, id)
        assert deleted != None



class TestDeleteUser:
    
    
    def test_delete_author_with_post(self, db):
        post = retrieve_from_database(Post, db, author_id=5)
        assert len(post) == 1
        deleted_user = delete_record(User, db, 5)
        
        post = retrieve_from_database(Post, db, author_id=5)
        
        assert len(post) == 0
    
    def test_post_deleted(self, db):
        post = retrieve_from_database(Post, db, author_id=5)
        assert len(post) == 1
        post_id = post[0].id
        
        delete_record(User, db, 5)
        
        post = retrieve_from_database(Post, db, id=post_id)
        assert len(post) == 0
        