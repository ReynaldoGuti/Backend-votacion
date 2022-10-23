from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa
class ControladorResultados():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()
    def index(self):
        return self.repositorioResultado.findAll()
    def create(self, dataResultados,id_candidato,id_mesa):
        nuevosResultados = Resultado(dataResultados)
        candidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        mesa = Mesa(self.repositorioMesa.findById(id_mesa))
        nuevosResultados.candidato = candidato
        nuevosResultados.mesa = mesa
        return self.repositorioResultado.save(nuevosResultados)
    def show(self, id):
        resultado = Resultado(self.repositorioResultado.findById(id))
        return resultado.__dict__

    def update(self,dataResultados,id,id_candidato,id_mesa):
        resultadoActualizado = Resultado(self.repositorioResultado.findById(id))
        resultadoActualizado.numero_votos = dataResultados["numeros_votos"]
        resultadoActualizado.numero_mesa = dataResultados["numero_mesa"]
        resultadoActualizado.cedula_candidato = dataResultados["cedula_candidato"]
        candidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        mesa = Mesa(self.repositorioMesa.findById(id_mesa))
        resultadoActualizado.candidato = candidato
        resultadoActualizado.mesa = mesa
        return self.repositorioResultado.save(resultadoActualizado)

    def delete(self, id):
        return self.repositorioResultado.delete(id)