from flask import Response, request
from database.diagnostico import Diagnostico
from flask_restful import Resource

class DiagnosticoApi(Resource):
    def get(self):
        diagnostico = Diagnostico.objects().to_json()
        return Response(diagnostico, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        diagnostico = Diagnostico(**body).save()
        id = diagnostico.id
        return {'id': str(id)}, 200

class DiagnosticosApi(Resource):
    def put(self, id):
        body = request.get_json()
        Diagnostico.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        diagnostico = Diagnostico.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        try:
            diagnostico = Diagnostico.objects.get(id=id).to_json()
            return Response(diagnostico, mimetype="application/json", status=200)
        except Exception as error:
            return Response(error, status=400, mimetype='application/json')
