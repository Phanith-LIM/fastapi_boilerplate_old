from pydantic import BaseModel


class CategoryModel(BaseModel):
    name: str
    description: str


class UpdateCategoryModel(CategoryModel):
    pass
