"""The main file"""
from fastapi import FastAPI

from connection.database import engine
from models.books_model import books

app = FastAPI(title="Book Store",
              description="The backend of a simple BookStore webapp")


@app.on_event("startup")
async def startup_event():
    """The startup event"""
    print("Connecting to Database")
    engine.connect()
    print("Connected to Database")


@app.on_event("shutdown")
async def shutdown_event():
    """The shutdown event"""
    print("Disconnecting from Database")
    engine.dispose()
    print("Disconnected from the engine")


@app.get("/", name="Root", description="The root endpoint of the API")
async def root() -> dict[str, str]:
    """The root endpoint of the API

    Returns:
        dict[str, str]: _description_
    """
    return {"Message": "The API Works"}


@app.get("/books", name="Get all books", description="Gets all books in the database")
async def get_all_books_endpoint():
    _all_books = books.select()
