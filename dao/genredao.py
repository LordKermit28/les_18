from dao.models.director import Director
from dao.models.genre import Genre


class GenreDao:
    def __init__(self, session):
        self.session = session
        self.model = Genre

    def get_one(self, gid):

        return self.session.query(self.model).get(gid), 200

    def get_all(self):
        return self.session.query(self.model).all(), 200
