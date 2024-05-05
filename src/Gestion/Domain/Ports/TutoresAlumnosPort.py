from abc import ABC, abstractmethod
from src.Gestion.Domain.Entities.TutoresAlumnos import TuroresAlumnos


class TutoresAlumnosPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def getTuroresAlumnos(self, tutor_uuid):
        pass

    @abstractmethod
    def crearTuroresAlumnos(self, turoresAlumnos: TuroresAlumnos):
        pass