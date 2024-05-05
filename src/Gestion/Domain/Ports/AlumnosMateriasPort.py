from abc import ABC, abstractmethod
from src.Gestion.Domain.Entities.AlumnosMaterias import AlumnosMaterias


class AlumnosMateriasPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def getAlumnosMaterias(self):
        pass

    @abstractmethod
    def createAlumnosMaterias(self, alumnosMaterias: AlumnosMaterias):
        pass
