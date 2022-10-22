from Modelos.Candidato import Candidato
from Repositorios.RepositorioCandidato import RepositorioCandidato
class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
    def index(self):
        return self.repositorioCandidato.findAll()
    def create(self, dataCandidato):
        nuevoCandidato= Candidato(dataCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)
    def show(self, id):
        candidato= Candidato(self.repositorioCandidato.findById(id))
        return candidato.__dict__
    def update(self,id,dataCandidato):
        candidatoActualizado = Candidato(self.repositorioCandidato.findById(id))
        candidatoActualizado.cedula = dataCandidato["cedula"]
        candidatoActualizado.nombre = dataCandidato["nombre"]
        candidatoActualizado.apellido = dataCandidato["apellido"]
        candidatoActualizado.numero_resolucion= dataCandidato["numero_resolucion"]
        return self.repositorioCandidato.save(candidatoActualizado)
    def delete(self, id):
        return self.repositorioCandidato.delete(id)