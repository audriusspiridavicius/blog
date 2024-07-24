from typing import TypeVar
from sqlalchemy.orm import Session

T = TypeVar("T")

def create(model: T, db:Session) -> T:
    
    db.add(model)
    db.commit()
    db.refresh(model)
    
    return model