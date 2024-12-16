from pydantic import BaseModel


# Base Schema that defines common attributes for all book-related schemas
class BookBase(BaseModel):
    title: str
    author: str
    published_year: int


# Schema for creating a new book
class BookCreate(BookBase):
    isbn: str


# Schema for updating a book
class BookUpdate(BookBase):
    isbn: str | None = None
    title: str | None = None
    author: str | None = None
    published_year: int | None = None


# Schema for returning book data - adds id field and configures ORM mode
class Book(BookBase):
    id: int
    isbn: str

    class Config:
        from_attributes = True
