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
    def put(self, codDiagnostico):
        body = request.get_json()
        Diagnostico.objects.get(codDiagnostico=codDiagnostico).update(**body)
        return 'Se actualizo el diagnostico', 200

    def delete(self, codDiagnostico):
        diagnostico = Diagnostico.objects.get(codDiagnostico=codDiagnostico).delete()
        return 'Se elimino el diagnostico', 200

    def get(self, codDiagnostico):
        try:
            diagnostico = Diagnostico.objects.get(codDiagnostico=codDiagnostico).to_json()
            return Response(diagnostico, mimetype="application/json", status=200)
        except Exception as error:
            return Response(error, status=400, mimetype='application/json')
