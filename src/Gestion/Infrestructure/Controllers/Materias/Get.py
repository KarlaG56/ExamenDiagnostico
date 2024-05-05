from src.Gestion.Domain.Ports.MateriasPort import MateriasPort as Port
from src.Gestion.Aplication.UseCase.Materias.GetUseCase import GetUseCase as UseCase


class GetController:
    def __init__(self, port: Port):
        self.use_case = UseCase(port)

    def run(self):
        return self.use_case.run()
