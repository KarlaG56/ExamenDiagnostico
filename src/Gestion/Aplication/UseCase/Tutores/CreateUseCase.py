from src.Gestion.Domain.Entities.Turores import Tutores
from src.Gestion.Domain.Ports.TutoresPort import TutoresPort as Port


class CreateUseCase:
    def __init__(self, port: Port):
        self.repository = port

    def run(self, data):
        return self.repository.create_tutores(Tutores(**data))

