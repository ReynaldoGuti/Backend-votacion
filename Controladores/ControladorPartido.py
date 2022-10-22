from Modelos.Partido import Partido
from Repositorios.RepositorioPartido import RepositorioPartido

class ControladorPartido():
    def __init__(self):
        self.repositorioPartido = RepositorioPartido()
    def index(self):
        return self.repositorioPartido.findAll()
    def create(self, dataPartido):
        nuevoPartido= Partido(dataPartido)
        return self.repositorioPartido.save(nuevoPartido)
    def show(self, id):
        partido= Partido(self.repositorioPartido.findById(id))
        return partido.__dict__
    def update(self,id,dataPartido):
        partidoActualizado = Partido(self.repositorioPartido.findById(id))
        partidoActualizado.nombre = dataPartido["nombre"]
        partidoActualizado.lema = dataPartido["lema"]
        return self.repositorioPartido.save(partidoActualizado)
    def delete(self, id):
        return self.repositorioPartido.delete(id)