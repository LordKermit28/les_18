from dao.moviedao import MovieDao
from dao.directordao import DirectorDao
from dao.genredao import GenreDao
from dao.models.setup_db import db
from services.movieservices import MovieService
from services.directorservice import DirectorService
from services.genresirvice import GenreService


movie_dao = MovieDao(db.session)
movie_service = MovieService(movie_dao)


director_dao = DirectorDao(db.session)
director_service = DirectorService(director_dao)


genre_dao = GenreDao(db.session)
genres_service = GenreService(genre_dao)