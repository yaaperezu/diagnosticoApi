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
    def put(self, documenNumber):
        body = request.get_json()
        Paciente.objects.get(documenNumber=documenNumber).update(**body)
        return 'Se actualizo el paciente', 200

    def delete(self, documenNumber):
        patiens = Paciente.objects.get(documenNumber=documenNumber).delete()
        return 'Se eliminó el paciente correctamente', 200

    def get(self, documenNumber):
        try:
            patiens = Paciente.objects.get(documenNumber=documenNumber).to_json()
            return Response(patiens, mimetype="application/json", status=200)
        except Exception as error:
            return Response(error, status=400, mimetype='application/json')
