from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from .database import Base


class Post(Base):

    __tablename__ = "posts"
    
    id:Mapped[int] = mapped_column(primary_key=True, index=True)
    title:Mapped[str] = mapped_column(nullable=False)
    content:Mapped[str] = mapped_column(nullable=False)
    author_id:Mapped[int] = mapped_column(ForeignKey("users.id"))
    author:Mapped["User"] = relationship("User", back_populates="posts")