from src.Gestion.Domain.Ports.TutoresAlumnosPort import TutoresAlumnosPort as Port
from src.Gestion.Aplication.UseCase.TutoresAlumnos.CreateUseCase import CreateUseCase as UseCase


class CreateController:
    def __init__(self, port: Port):
        self.use_case = UseCase(port)

    def run(self, request):
        return self.use_case.run(request.get_json())
