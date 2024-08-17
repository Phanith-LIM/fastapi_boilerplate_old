import os
import argparse

# Define templates for files
TEMPLATES = {
    "controller": """from fastapi import APIRouter, Depends, HTTPException
from .service import MyService
from .model import MyModel

router = APIRouter()

@router.get("/")
async def get_items():
    # Implement your logic here
    pass

@router.post("/")
async def create_item(item: MyModel):
    # Implement your logic here
    pass
""",
    "model": """from pydantic import BaseModel

class MyModel(BaseModel):
    name: str
    value: int
""",
    "service": """class MyService:
    def __init__(self):
        # Initialize service
        pass

    def get_all(self):
        # Implement your logic here
        pass

    def create(self, item):
        # Implement your logic here
        pass
""",
    "entity": """from sqlalchemy import Column, Integer, String
from app.core.database import Base

class MyEntity(Base):
    __tablename__ = "my_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    value = Column(Integer)
"""
}


def create_file(file_type, directory):
    if file_type in TEMPLATES:
        file_name = f"{file_type}.py"
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'w') as file:
            file.write(TEMPLATES[file_type])
        print(f"Created {file_name} in {directory}")
    else:
        print(f"Unknown file type: {file_type}")


def main():
    parser = argparse.ArgumentParser(description='Generate project files.')
    parser.add_argument('file_type', type=str, help='Type of file to generate (controller, model, service, entity)')
    parser.add_argument('--directory', type=str, default='.', help='Directory to create the file in')

    args = parser.parse_args()

    if not os.path.exists(args.directory):
        os.makedirs(args.directory)

    create_file(args.file_type, args.directory)


if __name__ == "__main__":
    main()
