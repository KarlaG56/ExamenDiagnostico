import uuid


class Tutores:
    def __init__(self, nombre, apellido, horas, titulo):
        self.uuid = uuid.uuid4()
        self.nombre = nombre
        self.apellido = apellido
        self.horas = horas
        self.titulo = titulo
