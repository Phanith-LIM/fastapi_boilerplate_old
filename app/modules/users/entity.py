from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import deferred, relationship
from sqlalchemy.dialects.postgresql import ARRAY
from app.util.common.roles import UserRoles


class UserEntity(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = deferred(Column('hashedPassword', String))
    status = Column(Integer, index=True, default=1)
    roles = Column(ARRAY(String), default=lambda: [UserRoles.USER.value])
    created_at = Column('createAt', DateTime, server_default=func.now())
    updated_at = Column('updatedAt', DateTime, server_default=func.now(), onupdate=func.now())

    categories = relationship("CategoryEntity", back_populates="added_by")
