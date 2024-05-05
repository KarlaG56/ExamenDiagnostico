import uuid


class Alumnos:
    def __init__(self, nombre, apellido, grado, grupo):
        self.uuid = uuid.uuid4()
        self.nombre = nombre
        self.apellido = apellido
        self.grado = grado
        self.grupo = grupo
