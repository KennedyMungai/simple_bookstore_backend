"""The main file"""
from fastapi import FastAPI
from connection.database import metadata, engine


app = FastAPI(title="Book Store",
              description="The backend of a simple BookStore webapp")

@app.on_event("startup")
async def startup_event():
    """The startup event"""
    print("Connecting to Database")
    metadata.create_all(engine)
    engine.connect()
    print("Connected to Database")


@app.get("/", name="Root", description="The root endpoint of the API")
async def root() -> dict[str, str]:
    """The root endpoint of the API

    Returns:
        dict[str, str]: _description_
    """
    return {"Message": "The API Works"}
