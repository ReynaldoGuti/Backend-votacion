from Modelos.Mesa import Mesa
from Repositorios.RepositorioMesa import RepositorioMesa
class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()
    def index(self):
        return self.repositorioMesa.findAll()

    def create(self, dataMesa):
        nuevaMesa= Mesa(dataMesa)
        return self.repositorioMesa.save(nuevaMesa)

    def show(self, id):
        mesa= Mesa(self.repositorioMesa.findById(id))
        return mesa.__dict__

    def update(self,id,dataMesa):
        mesaActualizada = Mesa(self.repositorioMesa.findById(id))
        mesaActualizada.numero= dataMesa["numero"]
        mesaActualizada.cantidad_inscritos = dataMesa["cantidad_inscritos"]
        return self.repositorioMesa.save(mesaActualizada)

    def delete(self, id):
        return self.repositorioMesa.delete(id)
