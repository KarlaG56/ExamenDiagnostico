from src.Gestion.Aplication.UseCase.Tutores.GetUseCase import GetUseCase as UseCase
from src.Gestion.Domain.Ports.TutoresPort import TutoresPort as Port


class GetController:
    def __init__(self, port: Port):
        self.use_case = UseCase(port)

    def run(self):
        return self.use_case.run()
