import uuid


class Materias:
    def __init__(self, nombre):
        self.uuid = uuid.uuid4()
        self.nombre = nombre
