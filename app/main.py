from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.util.middleware.current_user import current_user_middleware
from app.modules.users.controller import router as user_router
from app.modules.categories.controller import router as category_router

app = FastAPI(
    title="FastAPI",
    description="This is my API",
    version="1.0.0",
    docs_url="/api/v1",
)

app.middleware("http")(current_user_middleware)
app.include_router(user_router)
app.include_router(category_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    # Create database tables
    # Base.metadata.create_all(bind=engine)
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
