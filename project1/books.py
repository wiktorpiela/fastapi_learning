from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get('/books/{book_title}')
async def read_book(book_title: str):
    for book in BOOKS:
        if book['title'].lower() == book_title.lower():
            return book

@app.get('/books/')
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book['category'].lower() == category.lower():
            books_to_return.append(book)
    return books_to_return


@app.get('/books/{book_author}/')
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book['category'].lower() == category.lower() and book['author'].lower() == book_author.lower():
            books_to_return.append(book)
    return books_to_return

@app.post('/books/create_book')
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put('/books/update_book/')
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i]['title'].lower() == updated_book['title'].lower():
            BOOKS[i] = updated_book

@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i]['title'].lower() == book_title.lower():
            BOOKS.pop(i)
            break

@app.get('/books-by-author/{book_author}/')
async def get_books_by_author_path(book_author: str):
    books_to_return = []
    for book in BOOKS:
        if book['author'].lower() == book_author.lower():
            books_to_return.append(book)
    return books_to_return

@app.get('/books-by-author/')
async def get_books_by_author_query(book_author: str):
    books_to_return = []
    for book in BOOKS:
        if book['author'].lower() == book_author.lower():
            books_to_return.append(book)
    return books_to_return
