from src.Gestion.Domain.Entities.AlumnosMaterias import AlumnosMaterias
from src.Gestion.Domain.Ports.AlumnosMateriasPort import AlumnosMateriasPort as Port


class CreateUseCase:
    def __init__(self, port: Port):
        self.repository = port

    def run(self, data):
        return self.repository.createAlumnosMaterias(AlumnosMaterias(**data))
