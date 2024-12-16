from pydantic import BaseModel


# Base Model of all books
class BookBase(BaseModel):
    title: str
    author: str
    published_year: int


class BookCreate(BookBase):
    isbn: str


class BookUpdate(BookBase):
    isbn: str | None = None
    title: str | None = None
    author: str | None = None
    published_year: int | None = None


# a book use base model from BookBase
class Book(BookBase):
    id: int
    isbn: str

    class Config:
        from_attributes = True
