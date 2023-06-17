from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MovieService():
    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result

    def get_movie(self, movie_id):
        result = self.db.query(MovieModel).filter(MovieModel.id == movie_id).first()
        return result
    
    def get_movies_by_cateogry(self, cateogry):
        result = self.db.query(MovieModel).filter(MovieModel.category == cateogry).all()
        return result

    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return 
    
    def update_movie(self, id_movie: int, data: Movie):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id_movie).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()
        return
    
    def delete_movie(self, id_movie: int):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id_movie).first()
        self.db.delete(movie)
        self.db.commit()
        return
