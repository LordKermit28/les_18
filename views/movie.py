from flask import request
from flask_restx import Namespace, Resource

from container import movie_service
from dao.models.model import movies_schema, movie_schema

movie_ns = Namespace("movies")

@movie_ns.route("/")
class MoviesView(Resource):
    def get(self):
        director = request.args.get('director_id')
        genre = request.args.get('genre_id')
        year = request.args.get('year')
        filters = {
            'director_id': director,
            'genre_id': genre,
            'year': year,
        }

        all_movies = movie_service.get_all(filters)
        result = movies_schema.dump(all_movies)
        return result, 200

    def post(self):
        req_data = request.json
        movie_service.create(req_data)
        return "", 201


@movie_ns.route("/<int:mid>")
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        movie_data = movie_schema.dump(movie)
        return movie_data, 200

    def put(self, mid):
        req_data = request.json
        req_data['id'] = mid
        movie_service.update(req_data)
        return "", 203

    def delete(self, mid):
        movie_service.delete(mid)
        return "", 204




