
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from blogApp.database.database import Base
from blogApp.database import *
import pytest
SQLALCHEMY_DATABASE_URL_TEST = "sqlite:///test_db.db"

test_engine = create_engine(
    SQLALCHEMY_DATABASE_URL_TEST,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

@pytest.fixture(scope="session", autouse=True)
def get_test_database():
    Base.metadata.create_all(bind=test_engine)
    db = TestingSessionLocal()
    User.create_init_users(db)
    yield db

    Base.metadata.drop_all(bind=test_engine)
    db.close()

def test_database():
    Base.metadata.create_all(bind=test_engine)
    db = TestingSessionLocal()
    User.create_init_users(db)
    yield db

    Base.metadata.drop_all(bind=test_engine)
    db.close()
