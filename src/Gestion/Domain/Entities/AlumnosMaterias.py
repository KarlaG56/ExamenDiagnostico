import uuid


class AlumnosMaterias:
    def __init__(self, alumno_uuid, materia_uuid):
        self.uuid = uuid.uuid4()
        self.alumno_uuid = alumno_uuid
        self.materia_uuid = materia_uuid
