from sqlalchemy.orm import Session, joinedload, load_only
from fastapi import Depends, status, HTTPException
from app.core.database import get_db
from app.modules.users.entity import UserEntity
from app.util.common.roles import UserRoles
from .entity import CategoryEntity
from .model import CategoryModel
from typing import Type


class CategoryService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Type[CategoryEntity]]:
        return (
            self.db.query(CategoryEntity)
            .filter(0 != CategoryEntity.status)
            .options(load_only(CategoryEntity.id, CategoryEntity.name,
                               CategoryEntity.description))  # Limit columns for CategoryEntity if needed
            .all()
        )

    def get_by_id(self, category_id: int) -> Type[CategoryEntity]:
        category = (self.db.query(CategoryEntity).filter(category_id == CategoryEntity.id)
                    .options(joinedload(CategoryEntity.added_by)
                             .load_only(UserEntity.id, UserEntity.name))
                    .first())
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return category

    def create(self, category: CategoryModel, user: UserEntity) -> CategoryEntity:
        category_entity = CategoryEntity(
            name=category.name,
            description=category.description,
            user_id=user.id,
        )
        self.db.add(category_entity)
        self.db.commit()
        self.db.refresh(category_entity)
        return category_entity

    def update(self, category_id: int, update_cat: CategoryModel, user: UserEntity) -> CategoryEntity:
        category = self.db.query(CategoryEntity).get(category_id)
        if not category:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        if UserRoles.ADMIN.value in user.roles:
            category.name = update_cat.name
            category.description = update_cat.description
        elif UserRoles.USER.value in user.roles:
            if category.user_id != user.id:
                raise HTTPException(status.HTTP_403_FORBIDDEN)
            category.name = update_cat.name
            category.description = update_cat.description
        self.db.commit()
        self.db.refresh(category)
        return category

    def delete_category(self, category_id: int, user: UserEntity) -> Type[CategoryEntity]:
        category = self.db.query(CategoryEntity).get(category_id)
        if not category:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        if UserRoles.ADMIN.value in user.roles:
            category.status = 0
        elif UserRoles.USER.value in user.roles:
            if category.user_id != user.id:
                raise HTTPException(status.HTTP_403_FORBIDDEN)
            category.status = 0
        self.db.commit()
        self.db.refresh(category)
        return category


def get_category_service(db: Session = Depends(get_db)) -> CategoryService:
    return CategoryService(db=db)
