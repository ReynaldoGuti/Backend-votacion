from Modelos.Ciudadano import Ciudadano

class ControladorCiudadano():
    def __init__(self):
        print("Creando ControladorCiudadano")

    def index(self):
        print("Listando todos los ciudadanos")
        ciudadanos=[
            {"id": 1, "nombre": "juan", "apellido": "perez", "cedula": "123354212"},
            {"id": 2, "nombre": "reynaldo", "apellido": "gutierrez", "cedula": "12354520"},
            {"id": 3, "nombre": "luis", "apellido": "robado", "cedula": "4865636585"},
        ]
        return ciudadanos

    def create(self, dataCiudadano):
        print("Crear nuevo usuario Ciudadano")
        ciudadano = Ciudadano(dataCiudadano)
        return ciudadano.__dict__


    def show(self, id):
        print("Mostrando un ciudadano con id ", id)
        ciudadano = {
            "_id": id,
            "cedula": "123",
            "nombre": "Juyan",
            "apellido": "Perez"
        }
        return ciudadano

    def update(self,id,dataCiudadano):
        print("Actualizando usuario Ciudadano con id ", id)
        ciudadano = Ciudadano(dataCiudadano)
        return ciudadano.__dict__

    def delete(self, id):
        print("Eliminando usuario Ciudadano con id", id)
        return {"Cuenta Borrada":1}