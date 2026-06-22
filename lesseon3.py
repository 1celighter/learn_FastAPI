from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

books = [
    {
        "id": 1,
        "name": "Космос что идет за планетами?",
        "author": "James Anthony"
    },
    {
        "id": 2,
        "name": "Искуство в облоках",
        "author": "Lukas Kenade"
    }
]

@app.get(
    path="/books",
    tags=["Книги"],
    summary="Получить все книги"
)
def library():
    return books

@app.get("/books/{book_id}",
    tags=["Книги"],
    summary="Получить отдельную книгу"
)
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="not found")

class NewBook(BaseModel):
    title: str
    author: str

@app.post("/books",
    tags=["Книги"],
    summary="Занести книгу в библиотеку")

def create_book(new_book: NewBook):
    books.append({
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author
    })
    return {f"Ваша книга с названием {new_book.title} и за авторством {new_book.author} добавлена"}


if __name__ == "__main__":
    uvicorn.run("lesseon3:app", reload=True)