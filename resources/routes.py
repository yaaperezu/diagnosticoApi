from .client import ClientsApi, ClientApi
from .paciente import PacienteApi,PacientesApi
from .diagnostico import DiagnosticoApi, DiagnosticosApi

def initialize_routes(api):
    api.add_resource(ClientsApi, '/api/clients')
    api.add_resource(ClientApi, '/api/client/<id>')

    api.add_resource(PacienteApi, '/api/patients')
    api.add_resource(PacientesApi, '/api/patient/<documenNumber>')

    api.add_resource(DiagnosticoApi, '/api/diagnostics')
    api.add_resource(DiagnosticosApi, '/api/diagnostic/<codDiagnostico>')