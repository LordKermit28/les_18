from flask_restx import Namespace, Resource

from container import director_service
from dao.models.model import directors_schema, director_schema

director_ns = Namespace("directors")

@director_ns.route("/")
class MoviesView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        result = directors_schema.dump(all_directors)
        return result, 200


@director_ns.route("/<int:did>")
class MovieView(Resource):
    def get(self, did):
        movie = director_service.get_one(did)
        movie_data = director_schema.dump(movie)
        return movie_data, 200
