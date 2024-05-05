from src.Gestion.Aplication.UseCase.Alumnos.CreateUseCase import CreateUseCase
from src.Gestion.Domain.Ports.AlumnosPort import AlumnosPort


class CreateController:
    def __init__(self, repository: AlumnosPort):
        self.use_case = CreateUseCase(repository)

    def run(self, request):
        return self.use_case.run(request.get_json())
