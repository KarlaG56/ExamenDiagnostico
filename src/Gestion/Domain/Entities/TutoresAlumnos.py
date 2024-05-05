import uuid


class TuroresAlumnos:
    def __init__(self, alumno_uuid, tutor_uuid):
        self.uuid = uuid.uuid4()
        self.alumno_uuid = alumno_uuid
        self.tutor_uuid = tutor_uuid
