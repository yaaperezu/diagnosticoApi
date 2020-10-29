from .client import ClientsApi, ClientApi
from .paciente import PacienteApi

def initialize_routes(api):
    api.add_resource(ClientsApi, '/api/clients')
    api.add_resource(ClientApi, '/api/client/<id>')

    api.add_resource(PacienteApi, '/api/paciente')