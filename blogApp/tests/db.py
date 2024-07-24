
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from blogApp.database.database import Base
from blogApp.database import *

SQLALCHEMY_DATABASE_URL_TEST = "sqlite:///test_db.db"

test_engine = create_engine(
    SQLALCHEMY_DATABASE_URL_TEST,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


def get_test_database():
    Base.metadata.create_all(bind=test_engine)
    db = TestingSessionLocal()
    User.create_init_users(db)
    try:
        yield db
    finally:
        db.close()
