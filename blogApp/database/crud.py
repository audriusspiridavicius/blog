from typing import List, TypeVar, Iterable
from sqlalchemy.orm import Session

from blogApp.database import User, Post

DatabaseModel = TypeVar("DatabaseModel")


def remove_redundant_properties(model:DatabaseModel, properties:dict) -> dict:
    # remove those properties which do not exist in model Class
    values = {}
    for arg in properties:
        if arg in model.__dict__.keys():
            values[arg] = properties[arg]
    return values
    
def create(model, db:Session) -> DatabaseModel:
    
    db.add(model)
    db.commit()
    db.refresh(model)
    
    return model


def retrieve_from_database(model:DatabaseModel, db:Session, **kwargs) -> list[DatabaseModel]:
    """Get item from database

    Args:
        model: _description_
        db (Session): _description_
        **kwargs: dictionary of model property values on which it will be filtered. if passed property downt exist in model it will be ignored

    Returns:
        filtered results or empty list
    """
    return db.query(model).filter_by(**remove_redundant_properties(model, kwargs)).all()

def get_user_posts(db:Session, user_id:int) -> List[Post] | None:
    user = retrieve_from_database(User,db,id=user_id)
    if user:
        return user[0].posts 
    
    return None

def delete_record(model:DatabaseModel, db:Session, id:int) -> DatabaseModel | None:
    """Delete record from database"""
    
    record = db.query(model).filter_by(id=id).first()
    if record:
        db.delete(record)
        db.commit()
        return record
    
    return None