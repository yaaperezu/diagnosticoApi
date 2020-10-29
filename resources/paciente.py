from flask import Response, request
from database.paciente import Paciente
from flask_restful import Resource

class PacienteApi(Resource):
    def get(self):
        clients = Paciente.objects().to_json()
        return Response(clients, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        client = Paciente(**body).save()
        id = client.id
        return {'id': str(id)}, 200
