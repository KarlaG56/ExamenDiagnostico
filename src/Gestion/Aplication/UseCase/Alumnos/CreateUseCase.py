from src.Gestion.Domain.Entities.Alumnos import Alumnos
from src.Gestion.Domain.Ports.AlumnosPort import AlumnosPort


class CreateUseCase:
    def __init__(self, port: AlumnosPort):
        self.repository = port

    def run(self, data):
        return self.repository.createAlumnos(Alumnos(**data))
