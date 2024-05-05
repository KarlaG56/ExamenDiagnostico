import uuid


class TuroresAlumnos:
    def __init__(self, alumno_uuid, tutore_uuid):
        self.uuid = uuid.uuid4()
        self.alumno_uuid = alumno_uuid
        self.tutore_uuid = tutore_uuid
