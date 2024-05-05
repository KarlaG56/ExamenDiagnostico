from src.Gestion.Domain.Ports.AlumnosMateriasPort import AlumnosMateriasPort as Port


class GetUseCase:
    def __init__(self, port: Port):
        self.repository = port

    def run(self, alumno_uuid):
        return self.repository.getAlumnosMaterias(alumno_uuid)
