from src.Gestion.Domain.Entities.Alumnos import Alumnos
from abc import ABC, abstractmethod


class AlumnosPort(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def getAlumnos(self):
        pass

    @abstractmethod
    def createAlumnos(self, alumno:Alumnos):
        pass
