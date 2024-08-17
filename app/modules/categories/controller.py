from fastapi import APIRouter, Depends, Request
from .service import CategoryService, get_category_service
from app.util.guard import AuthGuard, AuthorizeGuard
from app.util.common.roles import UserRoles
from .model import CategoryModel

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


@router.get("")
def get_items(category_service: CategoryService = Depends(get_category_service)):
    return category_service.get_all()


@router.get("/{id}")
def get_item(id: str, category_service: CategoryService = Depends(get_category_service)):
    return category_service.get_by_id(int(id))


@router.post("", dependencies=[Depends(AuthGuard())])
def create_item(cat: CategoryModel, req: Request, category_service: CategoryService = Depends(get_category_service)):
    return category_service.create(cat, req.state.current_user)


@router.put("/{id}", dependencies=[Depends(AuthGuard()), Depends(AuthorizeGuard([UserRoles.USER, UserRoles.ADMIN]))],
            response_model=CategoryModel)
def update(id: int, cat: CategoryModel, req: Request,
           category_service: CategoryService = Depends(get_category_service)):
    return category_service.update(id, cat, req.state.current_user)


@router.delete(path='/{id}',
               dependencies=[Depends(AuthGuard()), Depends(AuthorizeGuard([UserRoles.USER, UserRoles.ADMIN]))],
               response_model=CategoryModel)
def delete_category(id: int, req: Request, category_service: CategoryService = Depends(get_category_service)):
    return category_service.delete_category(id, req.state.current_user)
