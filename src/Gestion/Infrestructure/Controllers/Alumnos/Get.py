from src.Gestion.Aplication.UseCase.Alumnos.GetUseCase import GetUseCase
from src.Gestion.Domain.Ports.AlumnosPort import AlumnosPort


class GetController:
    def __init__(self, repository: AlumnosPort):
        self.use_case = GetUseCase(repository)

    def run(self):
        return self.use_case.run()
