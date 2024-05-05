from src.Gestion.Domain.Ports.MateriasPort import MateriasPort as Port
from src.Gestion.Aplication.UseCase.Materias.CreateUseCase import CreateUseCase as UseCase


class CreateController:
    def __init__(self, port: Port):
        self.use_case = UseCase(port)

    def run(self, request):
        return self.use_case.run(request.get_json())
