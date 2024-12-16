from fastapi import FastAPI
from .routes import book_router
from .database import engine, Base
from .config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.include_router(book_router, prefix="/books", tags=["books"])


@app.get("/", tags=["root"])
def read_root():
    return {"message": "Welcome to book management system", "documentaion": "/docs"}
