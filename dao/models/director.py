from marshmallow import Schema, fields

from dao.models.setup_db import db



class Director(db.Model):
    __tablename__ = "director"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()