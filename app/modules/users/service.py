from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from .model import CreateUserModel, SignInUserModel, SignUpUserModel
from .entity import UserEntity
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from typing import Optional, List, Type

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"


class UserService:
    def __init__(self, db: Session, pwd_context: CryptContext):
        self.db = db
        self.pwd_context = pwd_context

    def create_user(self, user: CreateUserModel) -> UserEntity:
        new_user = UserEntity(
            name=user.name,
            email=user.email,
            hashed_password=self.pwd_context.hash(user.password),
            roles=[role.value for role in user.roles]
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def get_all(self) -> list[Type[UserEntity]]:
        return self.db.query(UserEntity).all()

    def sign_in(self, user: SignInUserModel) -> str:
        existing_user: Optional[UserEntity] = self.db.query(UserEntity).filter_by(email=user.email).first()
        if not existing_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        if not self.pwd_context.verify(user.password, existing_user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
        return self.generate_token(existing_user.id, roles=existing_user.roles)

    def find_one(self, id: int) -> UserEntity:
        user: Optional[UserEntity] = self.db.query(UserEntity).get(id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

    async def sign_up(self, user: SignUpUserModel) -> UserEntity:
        new_user = UserEntity(
            name=user.name,
            email=user.email,
            hashed_password=self.pwd_context.hash(user.password),
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    @staticmethod
    def generate_token(user_id: int, expires_delta: Optional[timedelta] = None, roles: Optional[List[str]] = None) -> str:
        expire = datetime.now() + (expires_delta or timedelta(minutes=30))
        token_data = {
            "sub": str(user_id),
            "roles": roles,
            "exp": expire
        }
        encoded_jwt = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return UserService(db, pwd_context)
