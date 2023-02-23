from dao.models.director import Director


class DirectorDao:
    def __init__(self, session):
        self.session = session
        self.model = Director

    def get_one(self, did):

        return self.session.query(self.model).get(did), 200

    def get_all(self):
        return self.session.query(self.model).all(), 200
