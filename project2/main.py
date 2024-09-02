from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int


BOOKS = [
    Book(id=1, title="Book1", author="author1", description="Book 1 desc", rating=1),
    Book(id=2, title="Book2", author="author1", description="Book 2 desc", rating=4),
    Book(id=3, title="Book3", author="author2", description="Book 3 desc", rating=3),
    Book(id=4, title="Book4", author="author2", description="Book 4 desc", rating=5),
    Book(id=5, title="Book5", author="author3", description="Book 5 desc", rating=1),
    Book(id=6, title="Book6", author="author3", description="Book 6 desc", rating=1),
]
@app.get('/books/')
async def read_all_books():
    return BOOKS

@app.post('/create-book/')
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)
    return new_book