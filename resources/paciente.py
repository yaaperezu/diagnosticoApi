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

class PacientesApi(Resource):
    def put(self, id):
        body = request.get_json()
        Paciente.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        patiens = Paciente.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        try:
            patiens = Paciente.objects.get(id=id).to_json()
            return Response(patiens, mimetype="application/json", status=200)
        except Exception as error:
            return Response(error, status=400, mimetype='application/json')
