from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from database import BookDatabaseManager

app = FastAPI(
    title="Book Data Pipeline API",
    description="FastAPI microservice for the first 20 books scraped from Books to Scrape.",
    version="1.0.0"
)

db = BookDatabaseManager("books.db")

class BookInput(BaseModel):
    title: str = Field(..., min_length=1)
    price: float = Field(..., ge=0)
    in_stock: bool
    rating: int = Field(..., ge=1, le=5)

class Book(BookInput):
    id: int

@app.get("/books", response_model=list[Book])
def get_books():
    return db.get_books()

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = db.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books", response_model=Book, status_code=201)
def create_book(book: BookInput):
    book_id = db.create_book(
        book.title, book.price, book.in_stock, book.rating
    )
    return db.get_book(book_id)

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookInput):
    if not db.get_book(book_id):
        raise HTTPException(status_code=404, detail="Book not found")

    db.update_book(
        book_id, book.title, book.price, book.in_stock, book.rating
    )
    return db.get_book(book_id)

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if not db.delete_book(book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully", "id": book_id}
