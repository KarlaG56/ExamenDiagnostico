from src.Gestion.Domain.Entities.TutoresAlumnos import TuroresAlumnos
from src.Gestion.Domain.Ports.TutoresAlumnosPort import TutoresAlumnosPort as Port


class CreateUseCase:
    def __init__(self, port: Port):
        self.repository = port

    def run(self, data):
        try:
            return self.repository.crearTuroresAlumnos(TuroresAlumnos(**data))
        except Exception as e:
            return {"error": str(e)}, 404
