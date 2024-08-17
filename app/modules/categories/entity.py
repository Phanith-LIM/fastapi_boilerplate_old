from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class CategoryEntity(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(String)
    status = Column(Integer, index=True, default=1)
    created_at = Column('createAt', DateTime, server_default=func.now())
    updated_at = Column('updatedAt', DateTime, server_default=func.now(), onupdate=func.now())

    user_id = Column('userId', Integer, ForeignKey('users.id'))
    added_by = relationship("UserEntity", back_populates="categories")
