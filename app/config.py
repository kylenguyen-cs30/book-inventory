# app/config


class Settings:
    # NOTE: project metadata
    PROJECT_NAME: str = "Book Management System"
    PROJECT_VERSION: str = "1.0.0"

    # NOTE: Database configurations
    MYSQL_USER: str = "kyle"
    MYSQL_PASSWORD: str = "password123"
    MYSQL_HOST: str = "db"
    MYSQL_PORT: int = 3306
    MYSQL_DATABASE: str = "book_management"
    DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"


settings = Settings()
