from fastapi import FastAPI
from .routes import book_router
from .database import engine, Base
from .config import settings

# NOTE: define project metadata
Base.metadata.create_all(bind=engine)

# NOTE: create FastAPI configuration
app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

# NOTE: define router
app.include_router(book_router, prefix="/books", tags=["books"])

# NOTE: Health check route
@app.get("/", tags=["root"])
def read_root():
    return {"message": "Welcome to book management system", "documentaion": "/docs"}
