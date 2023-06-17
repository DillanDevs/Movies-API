from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI(
    title="My First API",
    description="This is my first API with FastAPI",
    version="0.1.0",
)

app.add_middleware(ErrorHandler)

app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)

movies = [
    {
        "id": 1,
        "title": "The Godfather",
        "overview": "Spanning the years 1945 to 1955, a chronicle of the fictional Italian-American Corleone crime family.",
        "year": 1972,
        "rating": 9.2,
        "category": "Crime",
    },
    {
        "id": 2,
        "title": "The Godfather: Part II",
        "overview": "In the continuing saga of the Corleone crime family, a young Vito Corleone grows up in Sicily and in 1910s New York.",
        "year": 1974,
        "rating": 9.0,
        "category": "Crime",
    }
]



@app.get("/", tags=["Root"])
def message():
    return HTMLResponse(content="<h1>Welcome to my API</h1>")
