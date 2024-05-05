from src.Gestion.Domain.Ports.TutoresAlumnosPort import TutoresAlumnosPort as Port
from src.Gestion.Aplication.UseCase.TutoresAlumnos.GetUseCase import GetUseCase as UseCase


class GetController:
    def __init__(self, port: Port):
        self.use_case = UseCase(port)

    def run(self, tutor_uuid):
        return self.use_case.run(tutor_uuid)
