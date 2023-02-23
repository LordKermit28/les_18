from dao.models.director import DirectorSchema
from dao.models.genre import GenreSchema
from dao.models.movie import MovieSchema

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)



director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)