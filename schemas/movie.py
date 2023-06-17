from typing import Optional
from pydantic import BaseModel, Field


class Movie(BaseModel):
    id : Optional[int] = None
    title : str = Field(min_length = 5, max_length=15)
    overview : str = Field(min_length = 15, max_length=1000)
    year : int = Field(le=2022)
    rating : float = Field(ge=1, le=10.0)
    category : str = Field(min_length = 3, max_length=15)

    class Config:
        schema_extra = {
            "example": {
                "title": "The Godfather",
                "overview": "Spanning the years 1945 to 1955, a chronicle of the fictional Italian-American Corleone crime family.",
                "year": 1972,
                "rating": 9.2,
                "category": "Crime",
            }
        }

