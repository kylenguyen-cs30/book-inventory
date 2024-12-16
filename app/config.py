# app/config


class Settings:
    PROJECT_NAME: str = "Book Management System"
    PROJECT_VERSION: str = "1.0.0"
    MYSQL_USER: str = "kyle"
    MYSQL_PASSWORD: str = "password123"
    MYSQL_HOST: str = "db"
    MYSQL_PORT: int = 3306
    MYSQL_DATABASE: str = "book_management"
    DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"


settings = Settings()


"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Book Management System"
    PROJECT_VERSION: str = "1.0.0"
    MYSQL_USER: str = "kyle"
    MYSQL_PASSWORD: str = "password123"
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_DATABASE: str = "book_management"
    DATABASE_URL: str = None  # Add type annotation

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.DATABASE_URL = f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"


settings = Settings()
"""
