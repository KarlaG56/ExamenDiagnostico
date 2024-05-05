from src.Gestion.Domain.Ports.AlumnosMateriasPort import AlumnosMateriasPort as Port
from src.Gestion.Aplication.UseCase.AlumnosMaterias.GetUseCase import GetUseCase as UseCase


class GetController:
    def __init__(self, port: Port):
        self.use_case = UseCase(port)

    def run(self, alumno_uuid):
        return self.use_case.run(alumno_uuid)
