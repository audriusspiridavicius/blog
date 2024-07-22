from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///auth.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_database():
    from blogApp.database.user import User
    Base.metadata.create_all(bind=engine)
    try:
        db = SessionLocal()
        User.create_init_users(db)
        yield db
    finally:
        db.close()
        
