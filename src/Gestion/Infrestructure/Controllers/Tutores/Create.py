from src.Gestion.Domain.Ports.TutoresPort import TutoresPort as Port
from src.Gestion.Aplication.UseCase.Tutores.CreateUseCase import CreateUseCase as UseCase


class CreateController:
    def __init__(self, port: Port):
        self.use_case = UseCase(port)

    def run(self, request):
        return self.use_case.run(request.get_json())

