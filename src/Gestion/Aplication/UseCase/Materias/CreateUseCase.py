from src.Gestion.Domain.Entities.Materias import Materias
from src.Gestion.Domain.Ports.MateriasPort import MateriasPort as Port


class CreateUseCase:
    def __init__(self, port: Port):
        self.repository = port

    def run(self, data):
        return self.repository.createMaterias(Materias(**data))
