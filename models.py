from app.core.database import Base
from app.modules.users.entity import UserEntity
from app.modules.categories.entity import CategoryEntity
# Import your entities/models here if needed


# Use Base.metadata directly
target_metadata = Base.metadata
