from flask_restx import Namespace, Resource

from container import genres_service
from dao.models.model import genres_schema, genre_schema

genre_ns = Namespace("genre")

@genre_ns.route("/")
class GenreView(Resource):
    def get(self):
        all_genres = genres_service.get_all()
        result = genres_schema.dump(all_genres)
        return result, 200


@genre_ns.route("/<int:did>")
class GenreView(Resource):
    def get(self, did):
        movie = genres_service.get_one(did)
        movie_data = genre_schema.dump(movie)
        return movie_data, 200
