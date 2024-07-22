
from .database import Base, engine, SessionLocal
from . import *
def get_database():

    Base.metadata.create_all(bind=engine)
    try:
        db = SessionLocal()
        User.create_init_users(db)
        yield db
    finally:
        db.close()