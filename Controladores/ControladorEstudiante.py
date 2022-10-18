from Modelos.Estudiante import Estudiante

class ControladorEstudiante():
    def __init__(self):
        print("Creando ControladorEstudiante")

    def index(self):
        print("Listar todos los estudiantes")
        unEstudiante=[
            {"id": 1, "nombre": "juan", "apellido": "perez", "cedula": "123354212"},
            {"id": 2, "nombre": "reynaldo", "apellido": "gutierrez", "cedula": "12354520"},
            {"id": 3, "nombre": "luis", "apellido": "robado", "cedula": "4865636585"},
        ]
        return unEstudiante

    def create(self, infoEstudiante):
        print("Crear nuevo estudiante")
        elEstudiante= Estudiante(infoEstudiante)
        return elEstudiante.__dict__

    def show(self, id):
        print("Mostrando un estudiante con id ", id)
        elEstudiante = {
            "_id": id,
            "cedula": "123",
            "nombre": "Juyan",
            "apellido": "Perez"
        }
        return {"Hola estudiante con nombre":"Juyan"}

    def update(self,id,infoEstudiante):
        print("Actualizando estudiante con id ", id)
        elEstudiante = Estudiante(infoEstudiante)
        return elEstudiante.__dict__

    def delete(self, id):
        print("Eliminando estudiante con id", id)
        return {"deleted_count":1}