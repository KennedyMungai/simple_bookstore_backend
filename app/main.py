from fastapi import FastAPI


app = FastAPI(title="Book Store",
              description="The backend of a simple BookStore webapp")


@app.get("/", name="Root", description="The root endpoint of the API")
async def root() -> dict[str, str]:
    return {"Message": "The API Works"}
