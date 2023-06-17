from fastapi import APIRouter
from fastapi import Query, Path, Depends
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
from config.database import Session
from models.movie import Movie as MovieModel
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()


@movie_router.get("/movies", tags=["Movies"], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())]) 
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))


@movie_router.get("/movies/{movie_id}", tags=["Movies"], response_model=Movie)
def get_movie(movie_id: int = Path(ge=1, le=5000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(movie_id)
    if not result:
        return JSONResponse(status_code=404,content={"message": "Movie with id {} is not available.".format(movie_id)})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))    

@movie_router.get("/movies/", tags=["Movies"] , response_model=List[Movie])
def get_movies_by_cateogry(cateogry: str = Query(min_length=3, max_length=15)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies_by_cateogry(cateogry)
    if not result:
        return JSONResponse(status_code=404,content={"message": "Movie with category {} is not available.".format(cateogry)})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))
    

@movie_router.post("/movies", tags=["Movies"], response_model=dict, status_code=201)
def add_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Movie has been added."})
    

@movie_router.put("/movies/{movie_id}", tags=["Movies"] , response_model=dict, status_code=200)
def update_movie(movie_id: int, movie: Movie) -> dict:
    db = Session()
    result = MovieService(db).get_movie(movie_id)
    if not result:
        return JSONResponse(status_code=404,content={"message": "Movie with id {} is not available.".format(movie_id)})
    MovieService(db).update_movie(movie_id, movie)
    return JSONResponse(status_code=200,content={"message": "Movie with id {} has been updated.".format(movie_id)})


@movie_router.delete("/movies/{movie_id}", tags=["Movies"], response_model=dict, status_code=200)
def delete_movie(movie_id: int) -> dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    if not result:
        return JSONResponse(status_code=404,content={"message": "Movie with id {} is not available.".format(movie_id)})
    MovieService(db).delete_movie(movie_id)
    return JSONResponse(status_code=200, content={"message": "Movie with id {} has been deleted.".format(movie_id)})
