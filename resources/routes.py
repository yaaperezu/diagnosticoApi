from .client import ClientsApi, ClientApi
from .paciente import PacienteApi,PacientesApi
from .diagnostico import DiagnosticoApi, DiagnosticosApi

def initialize_routes(api):
    api.add_resource(ClientsApi, '/api/clients')
    api.add_resource(ClientApi, '/api/client/<id>')

    api.add_resource(PacienteApi, '/api/patient')
    api.add_resource(PacientesApi, '/api/patients/<id>')

    api.add_resource(DiagnosticoApi, '/api/diagnosi')
    api.add_resource(DiagnosticosApi, '/api/diagnosis/<id>')