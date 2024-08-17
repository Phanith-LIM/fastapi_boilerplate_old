from pydantic import BaseModel, EmailStr, Field
from typing import List, Annotated
from app.util.common.roles import UserRoles


class SignInUserModel(BaseModel):
    email: EmailStr = Field(...)
    password: Annotated[str, Field(min_length=8)]


class CreateUserModel(SignInUserModel):
    name: str = Field(..., min_length=1)
    roles: List[UserRoles] = Field(default_factory=list)


class SignUpUserModel(SignInUserModel):
    name: str = Field(..., min_length=1)


class UserResponseModel(BaseModel):
    id: int
    name: str
    email: EmailStr
    roles: List[str]


class TokenResponseModel(BaseModel):
    type: str
    access_token: str
