# SuperFast CLI Tool

This CLI tool is designed for generating common file types used in FastAPI projects, such as controllers, models, services, and entities.

## Installation

## Installation

You can install the CLI tool via pip:

```sh
pip install superfast-cli
```
## Usage
Generate files based on file type and class name:
```sh
fast create FILE_TYPE CLASS_NAME [--directory DIRECTORY]
```
##### Arguments: 
- FILE_TYPE - The type of file to generate. Valid values are:
  - controller: Creates a controller file.
  - model: Creates a model file.
  - service: Creates a service file.
  - entity: Creates an entity file.
  - res: Creates all file types (controller, model, service, and entity).
- CLASS_NAME - The name of the class to generate the file for.
- Options: -d, --directory - Directory to create the file in. Default is the current directory.

## Example
### Controller
Creates a controller.py file in the current location. You can also specify a location:
```sh
fast create controller MyController
```
```shell
fast create controller MyController --directory app/category
```
Generated File: `controller.py`
```shell
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_items():
    # Implement your logic here
    pass

@router.post("/")
async def create_item():
    # Implement your logic here
    pass
```

### Model
Creates an `model.py` file:
```sh
fast create model Category
```
```shell
fast create model Category --directory app/category
```
Generated File: `model.py`
```shell
from pydantic import BaseModel

class CategoryModel(BaseModel):
    id: int
    name: str
    description: str
```

### Entity
Creates an `entity.py` file:
```sh
fast create entity Category
```
```shell
fast create entity Category --directory app/category
```
Generated File: `entity.py`
```shell
# entity.py
from sqlalchemy import Column, Integer, String
from database import Base

class CategoryEntity(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
```
### Service
Creates an `service.py` file:
```sh
fast create Service Category
```
```shell
fast create service Category --directory app/category
```
Generated File: `service.py`
```shell
# service.py
from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db


class CategoryService:
    def __init__(self, db: Session):
        self.db = db


def get_category_service(db: Session = Depends(get_db)) -> CategoryService:
    return CategoryService(db=db)
```

### Resource
Creates all file types (`controller.py`, `model.py`, `service.py`, and `entity.py`):
```sh
fast create res Category
```
```shell
fast create res Category --directory app/category
```
Generated Files
```shell
- controller.py
- service.py
- model.py
- entity.py
```