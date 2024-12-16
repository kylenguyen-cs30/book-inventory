from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.book import Book as BookModel
from ..schemas.book import Book as BookSchema, BookCreate, BookUpdate


router = APIRouter()


# NOTE: routing create a new book
@router.post("/", response_model=BookSchema)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = BookModel(**book.dict())
    db.add(db_book)
    try:
        db.commit()
        db.refresh(db_book)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    return db_book


# NOTE:  get all the books
@router.get("/", response_model=List[BookSchema])
def get_books(db: Session = Depends(get_db)):
    return db.query(BookModel).all()


# NOTE: get a book
@router.get("/{book_id}", response_model=BookSchema)
def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    # book not found
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


# NOTE: Update a book
@router.put("/{book_id}", response_model=BookSchema)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()

    # return if the book is not found
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    # Get only the fields that were actually provided
    update_data = book.model_dump(exclude_unset=True)

    # if the isbn the same as the current one, remove it
    if "isbn" in update_data and db_book.isbn == update_data["isbn"]:
        del update_data["isbn"]

    # mapping each attribute to the book
    for key, value in update_data.items():
        setattr(db_book, key, value)

    try:
        db.commit()
        db.refresh(db_book)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    return db_book


# NOTE: delete a book
@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not Found")
    try:
        db.delete(db_book)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"message": "Book delete succesfully"}
