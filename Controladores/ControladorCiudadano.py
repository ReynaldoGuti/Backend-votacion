from Modelos.Ciudadano import Ciudadano
from Repositorios.RepositorioCiudadano import RepositorioCiudadano
class ControladorCiudadano():
    def __init__(self):
        self.repositorioCiudadano = RepositorioCiudadano()
    def index(self):
        return self.repositorioCiudadano.findAll()
    def create(self, dataCiudadano):
        nuevoCiudadano= Ciudadano(dataCiudadano)
        return self.repositorioCiudadano.save(nuevoCiudadano)
    def show(self, id):
        ciudadano= Ciudadano(self.repositorioCiudadano.findById(id))
        return ciudadano.__dict__
    def update(self,id,dataCiudadano):
        ciudadanoActualizado = Ciudadano(self.repositorioCiudadano.findById(id))
        ciudadanoActualizado.cedula = dataCiudadano["cedula"]
        ciudadanoActualizado.nombre = dataCiudadano["nombre"]
        ciudadanoActualizado.apellido = dataCiudadano["apellido"]
        return self.repositorioCiudadano.save(ciudadanoActualizado)
    def delete(self, id):
        return self.repositorioCiudadano.delete(id)