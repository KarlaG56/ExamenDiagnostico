from abc import ABC, abstractmethod
from src.Gestion.Domain.Entities.AlumnosMaterias import AlumnosMaterias


class AlumnosMateriasPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def getAlumnosMaterias(self, alumno_uuid):
        pass

    @abstractmethod
    def createAlumnosMaterias(self, alumnosMaterias: AlumnosMaterias):
        pass
