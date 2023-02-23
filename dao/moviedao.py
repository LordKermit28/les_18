from dao.models.movie import Movie


class MovieDao:
    def __init__(self, session):
        self.session = session
        self.model = Movie

    def get_one(self, mid):

        return self.session.query(self.model).get(mid), 200

    def get_all(self, filters):
        if filters['director_id']:
            return self.session.query(self.model).filter_by(
                self.model.director_id == filters['director_id']
            ).all(), 200

        elif filters['genre_id']:
            return self.session.query(self.model).filter_by(
                self.model.genre_id == filters['genre_id']
            ).all(), 200

        elif filters['year']:
            return self.session.query(self.model).filter_by(
                self.model.year == filters['year']
            ).all(), 200

        return self.session.query(self.model).all()

    def create(self, data):
        movie = self.model(**data)
        self.session.add(movie)
        self.session.commit()

        return movie, 20


    def update(self, data):
        mid = data.pop("id")
        movie = self.get_one(mid)
        for field_name, field_value in data.items():
            setattr(movie, field_name, field_value)

        self.session.add(movie)
        self.session.commit()


    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()
        return "", 204
