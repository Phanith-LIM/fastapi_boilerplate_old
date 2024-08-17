from fastapi import APIRouter, Depends, Request, HTTPException, status
from typing import List
from .model import CreateUserModel, SignInUserModel, UserResponseModel, TokenResponseModel, SignUpUserModel
from .service import UserService, get_user_service
from app.util.guard.authentication import AuthGuard
from app.util.guard.authorization import AuthorizeGuard
from app.util.common.roles import UserRoles

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(path='', response_model=List[UserResponseModel], dependencies=[Depends(AuthGuard())])
async def get_all_users(user_service: UserService = Depends(get_user_service)):
    return user_service.get_all()


@router.post(path='', response_model=UserResponseModel, dependencies=[Depends(AuthGuard()), Depends(AuthorizeGuard([UserRoles.ADMIN]))])
async def create_user(user: CreateUserModel, user_service: UserService = Depends(get_user_service)):
    return user_service.create_user(user)


@router.post(path='/signIn', response_model=TokenResponseModel)
async def sign_in(user: SignInUserModel, user_service: UserService = Depends(get_user_service)):
    token = user_service.sign_in(user)
    return TokenResponseModel(type="Bearer", access_token=token)


@router.post(path='/signUp', response_model=UserResponseModel)
async def sign_up(user: SignUpUserModel, user_service: UserService = Depends(get_user_service)):
    return user_service.sign_up(user)


@router.get(path='/me', response_model=UserResponseModel, dependencies=[Depends(AuthGuard())])
async def get_current_user(req: Request):
    current_user = req.state.current_user
    if not current_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User not found")
    return current_user
