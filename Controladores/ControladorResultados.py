from Modelos.Resultado import Resultado
from Repositorios.RepositorioResultado import RepositorioResultado

class ControladorResultados():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
    def index(self):
        return self.repositorioResultado.findAll()

    def create(self, dataResultados):
        nuevosResultados = Resultado(dataResultados)
        return self.repositorioResultado.save(nuevosResultados)

    def show(self, id):
        resultado = Resultado(self.repositorioResultado.findById(id))
        return resultado.__dict__

    def update(self, id, dataResultados):
        resultadosActualizados = Resultado(self.repositorioResultado.findById(id))
        resultadosActualizados.numero_mesa = dataResultados["numero_mesa"]
        resultadosActualizados.cedula_candidato = dataResultados["cedula_candidato"]
        resultadosActualizados.numero_votos = dataResultados["numero_votos"]
        return self.repositorioResultado.save(resultadosActualizados)
    def delete(self, id):
        return self.repositorioResultado.delete(id)