from flask import Response, request
from database.paciente import Paciente
from flask_restful import Resource

class PacienteApi(Resource):
    def get(self):
        patiens = Paciente.objects().to_json()
        return Response(patiens, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        patiens = Paciente(**body).save()
        id = patiens.id
        return {'id': str(id)}, 200
