from .db import db

class Diagnostico(db.Document):
    codDiagnostico = db.StringField(required=True,unique=True)
    nomDiagnostico = db.StringField(required=True)
    lateraliad = db.StringField(required=True)
    genero = db.StringField(required=True)
    estado = db.StringField(required=True)