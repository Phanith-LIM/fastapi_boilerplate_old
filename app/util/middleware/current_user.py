from fastapi import Request
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.modules.users.service import UserService
from passlib.context import CryptContext
import jwt

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

# Instantiate CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def current_user_middleware(request: Request, call_next):
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        request.state.current_user = None
    else:
        try:
            token = auth_header.split(" ")[1]
            payload = jwt.decode(
                token,
                key=SECRET_KEY,
                algorithms=[ALGORITHM]
            )
            user_id = int(payload.get("sub"))

            # Get the database session
            db: Session = next(get_db())
            repo = UserService(db, pwd_context)
            user = repo.find_one(user_id)
            if user:
                request.state.current_user = user
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, Exception):
            request.state.current_user = None
    response = await call_next(request)
    return response
