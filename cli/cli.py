import os
import click

# Define the template content for each file type
TEMPLATES = {
    'controller': '''from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_items():
    # Implement your logic here
    pass

@router.post("/")
async def create_item():
    # Implement your logic here
    pass
''',
    'model': '''from pydantic import BaseModel

class {class_name}Model(BaseModel):
    name: str
''',
    'service': '''from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db

class {class_name}Service:
    def __init__(self, db: Session):
        self.db = db

def get_{class_name_snake}_service(db: Session = Depends(get_db)) -> {class_name}Service:
    return {class_name}Service(db=db)
''',
    'entity': '''from sqlalchemy import Column, Integer, String
from database import Base

class {class_name}Entity(Base):
    __tablename__ = "{table_name}"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
''',
}

# Define filenames for each file type
FILE_NAMES = {
    'controller': 'controller.py',
    'model': 'model.py',
    'service': 'service.py',
    'entity': 'entity.py',
}

def format_content(template_content, class_name, table_name):
    """Replace placeholders in template with actual values."""
    class_name_snake = class_name.lower()
    return template_content.format(
        class_name=class_name,
        class_name_snake=class_name_snake,
        table_name=table_name or class_name_snake
    )

@click.group()
def cli():
    """CLI for generating project files."""
    click.echo("CLI for generating project files.")
    click.echo("Available commands:")
    click.echo("  create - Generate files based on file type and class name")

@cli.command(help="Generate files based on file type and class name.")
@click.argument('file_type', type=click.Choice(['controller', 'model', 'service', 'entity', 'res'], case_sensitive=False))
@click.argument('class_name')
@click.option('--directory', '-d', default='.', help='Directory to create the file in')
def create(file_type, class_name, directory):
    """Generate files based on file_type and class_name."""
    if file_type in TEMPLATES:
        template_content = TEMPLATES[file_type]

        if file_type == 'entity':
            table_name = class_name.lower()
        else:
            table_name = None

        formatted_content = format_content(template_content, class_name, table_name)

        file_name = FILE_NAMES[file_type]
        file_path = os.path.join(directory, file_name)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(file_path, 'w') as file:
            file.write(formatted_content)
        click.echo(f"Created {file_name} in {directory}")
    elif file_type == 'res':
        for key, template in TEMPLATES.items():
            if key == 'entity':
                table_name = class_name.lower()
            else:
                table_name = None

            formatted_content = format_content(template, class_name, table_name)
            file_name = FILE_NAMES[key]
            file_path = os.path.join(directory, file_name)
            if not os.path.exists(directory):
                os.makedirs(directory)
            with open(file_path, 'w') as file:
                file.write(formatted_content)
            click.echo(f"Created {file_name} in {directory}")
    else:
        click.echo(f"Invalid file type '{file_type}'. Use one of {', '.join(TEMPLATES.keys())}.")

if __name__ == "__main__":
    cli()
