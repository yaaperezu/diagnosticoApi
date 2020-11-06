from .db import db

class Paciente(db.Document):
    documenNumber = db.StringField(required=True)
    name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    gender = db.StringField(required=True)
    birthDate = db.StringField(required=True)

